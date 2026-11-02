"""Tests for scripts/check_links.py using a throwaway local HTTP server."""

from __future__ import annotations

import contextlib
import http.server
import io
import os
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_links  # noqa: E402


class Handler(http.server.BaseHTTPRequestHandler):
    """Tiny local HTTP server covering every status code classified by check_links."""

    def do_HEAD(self) -> None:  # noqa: N802
        self.respond(head_only=True)

    def do_GET(self) -> None:  # noqa: N802
        self.respond(head_only=False)

    def respond(self, head_only: bool) -> None:
        path = self.path.split("?")[0].rstrip("/") or "/"
        routes = {
            "/ok": (200, None),
            "/deep/page": (200, None),
            "/missing": (404, None),
            "/gone": (410, None),
            "/blocked": (403, None),
            "/rate-limited": (429, None),
            "/boom": (500, None),
            "/moved-far": (302, "/deep/page"),
            "/no-head-405": (200, None),
            "/no-head-404": (200, None),
            "/": (200, None),
        }
        if path == "/no-head-405" and head_only:
            status, location = 405, None
        elif path == "/no-head-404" and head_only:
            status, location = 404, None
        else:
            status, location = routes.get(path, (404, None))

        self.send_response(status)
        if location:
            self.send_header("Location", location)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, *args) -> None:
        return


class HttpCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_address[1]}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def check(self, path: str, **kwargs):
        defaults = {"timeout": 5, "retries": 0, "sleep": lambda _seconds: None}
        defaults.update(kwargs)
        return check_links.check_http(self.base + path, **defaults)

    def test_ok(self):
        result = self.check("/ok")
        self.assertEqual(result.status, check_links.STATUS_OK)
        self.assertEqual(result.http_status, 200)

    def test_not_found_is_dead(self):
        result = self.check("/missing")
        self.assertEqual(result.status, check_links.STATUS_DEAD)
        self.assertEqual(result.http_status, 404)

    def test_gone_is_dead(self):
        self.assertEqual(self.check("/gone").status, check_links.STATUS_DEAD)

    def test_forbidden_is_blocked_not_dead(self):
        result = self.check("/blocked")
        self.assertEqual(result.status, check_links.STATUS_BLOCKED)
        self.assertIn("bot protection", result.detail)

    def test_rate_limit_is_blocked(self):
        self.assertEqual(self.check("/rate-limited").status, check_links.STATUS_BLOCKED)

    def test_server_error_is_error(self):
        result = self.check("/boom")
        self.assertEqual(result.status, check_links.STATUS_ERROR)

    def test_head_rejection_falls_back_to_get(self):
        self.assertEqual(self.check("/no-head-405").status, check_links.STATUS_OK)
        self.assertEqual(self.check("/no-head-404").status, check_links.STATUS_OK)

    def test_redirect_to_new_path_is_reported(self):
        result = self.check("/moved-far")
        self.assertEqual(result.status, check_links.STATUS_REDIRECT)
        self.assertIn("redirects to", result.detail)

    def test_retries_transient_errors(self):
        sleeps: list[float] = []
        result = self.check("/boom", retries=2, sleep=sleeps.append)
        self.assertEqual(result.status, check_links.STATUS_ERROR)
        self.assertEqual(result.attempts, 3)
        self.assertEqual(len(sleeps), 2)

    def test_dns_failure_is_error(self):
        result = check_links.check_http(
            "http://does-not-exist.invalid", timeout=2, retries=0, sleep=lambda _s: None
        )
        self.assertEqual(result.status, check_links.STATUS_ERROR)

    def test_sinkholed_domain_is_dead(self):
        fake_addrinfo = [(2, 1, 6, "", ("127.0.0.1", 0))]
        with mock.patch("socket.getaddrinfo", return_value=fake_addrinfo):
            result = check_links.check_http(
                "https://defunct.example.com/", timeout=2, retries=0, sleep=lambda _s: None
            )
        self.assertEqual(result.status, check_links.STATUS_DEAD)
        self.assertIn("loopback", result.detail)

    def test_chrome_webstore_published_and_removed(self):
        ext_url = (
            "https://chromewebstore.google.com/detail/professor-prebid/"
            "kdnllijdimhbledmfdbljampcdphcbdc"
        )
        with mock.patch.object(check_links, "_request", return_value=(302, "https://dl.google.com/crx")):
            ok = check_links.check_http(ext_url, timeout=2, retries=0, sleep=lambda _s: None)
        self.assertEqual(ok.status, check_links.STATUS_OK)

        with mock.patch.object(check_links, "_request", return_value=(404, "")):
            dead = check_links.check_http(ext_url, timeout=2, retries=0, sleep=lambda _s: None)
        self.assertEqual(dead.status, check_links.STATUS_DEAD)
        self.assertIn("Chrome Web Store", dead.detail)


class ClassificationTests(unittest.TestCase):
    def test_classify_status(self):
        self.assertEqual(check_links.classify_status(200), check_links.STATUS_OK)
        self.assertEqual(check_links.classify_status(204), check_links.STATUS_OK)
        self.assertEqual(check_links.classify_status(301), check_links.STATUS_REDIRECT)
        self.assertEqual(check_links.classify_status(404), check_links.STATUS_DEAD)
        self.assertEqual(check_links.classify_status(451), check_links.STATUS_DEAD)
        self.assertEqual(check_links.classify_status(403), check_links.STATUS_BLOCKED)
        self.assertEqual(check_links.classify_status(999), check_links.STATUS_BLOCKED)
        self.assertEqual(check_links.classify_status(503), check_links.STATUS_ERROR)

    def test_trivial_redirects(self):
        self.assertTrue(check_links.is_trivial_redirect("https://prebid.org", "https://www.prebid.org/"))
        self.assertTrue(check_links.is_trivial_redirect("http://prebid.org/x", "https://prebid.org/x/"))
        self.assertFalse(check_links.is_trivial_redirect("https://prebid.org", "https://prebid.org/docs"))
        self.assertFalse(check_links.is_trivial_redirect("https://prebid.org", "https://example.org"))
        self.assertFalse(check_links.is_trivial_redirect("https://prebid.org", ""))


class AllowlistTests(unittest.TestCase):
    def test_parsing_and_matching(self):
        path = Path(tempfile.mkdtemp()) / "allowlist.txt"
        path.write_text(
            "# comment\n"
            "linkedin.com  # login wall\n"
            "https://example.com/private  # path scoped\n"
            "*.reddit.com  # datacenter block\n",
            encoding="utf-8",
        )
        entries = check_links.load_allowlist(path)
        self.assertEqual([e.host for e in entries], ["linkedin.com", "example.com", "reddit.com"])
        self.assertIsNotNone(check_links.match_allowlist("https://www.linkedin.com/in/x", entries))
        self.assertIsNotNone(check_links.match_allowlist("https://www.reddit.com/r/adops/", entries))
        self.assertIsNotNone(check_links.match_allowlist("https://example.com/private/x", entries))
        self.assertIsNone(check_links.match_allowlist("https://example.com/public", entries))


class CollectionAndCliTests(unittest.TestCase):
    def test_local_only_passes_on_repo_markdown_files(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            code = check_links.run(
                [
                    str(ROOT / "README.md"),
                    str(ROOT / "CONTRIBUTING.md"),
                    "--local-only",
                    "--quiet",
                ]
            )
        self.assertEqual(code, 0, buf.getvalue())

    def test_broken_local_and_anchor_links_fail(self):
        directory = Path(tempfile.mkdtemp())
        path = directory / "README.md"
        path.write_text("# Heading\n\n[missing](nope.md) [bad](#nowhere)\n", encoding="utf-8")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            code = check_links.run([str(path), "--local-only"])
        self.assertEqual(code, 1)
        self.assertIn("nope.md", buf.getvalue())
        self.assertIn("#nowhere", buf.getvalue())

    def test_markdown_report_and_github_summary(self):
        directory = Path(tempfile.mkdtemp())
        path = directory / "README.md"
        output = directory / "report.md"
        summary = directory / "summary.md"
        summary.write_text("", encoding="utf-8")
        path.write_text("# T\n\n[gone](missing.md)\n", encoding="utf-8")

        previous = os.environ.get("GITHUB_STEP_SUMMARY")
        os.environ["GITHUB_STEP_SUMMARY"] = str(summary)
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                check_links.run(
                    [
                        str(path),
                        "--local-only",
                        "--format",
                        "markdown",
                        "--output",
                        str(output),
                        "--github-summary",
                    ]
                )
        finally:
            if previous is None:
                os.environ.pop("GITHUB_STEP_SUMMARY", None)
            else:
                os.environ["GITHUB_STEP_SUMMARY"] = previous

        self.assertIn("## Link check", output.read_text(encoding="utf-8"))
        self.assertIn("missing.md", summary.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
