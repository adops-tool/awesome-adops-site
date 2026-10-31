#!/usr/bin/env python3
"""Link checker for Awesome AdOps.

Checks every link in README.md and reports unreachable URLs.

Special handling:
  * Chrome Web Store listings are verified through the Chrome update service
    (clients2.google.com/service/update2), which returns a redirect for a
    published item and an error page for an item that was removed/delisted.
    This catches the common "This product is unavailable" case.
  * 401/403/405/429/503 responses are reported as warnings instead of
    failures, because they are frequently bot-protection rather than rot.

Usage:
    python3 scripts/check_links.py                 # check README.md
    python3 scripts/check_links.py --timeout 15    # slower networks
    python3 scripts/check_links.py --json out.json # machine-readable output

Exit code is 1 when at least one link is broken, 0 otherwise.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

README = "README.md"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36 AwesomeAdOpsLinkCheck/1.0"
)
WARN_STATUSES = {401, 403, 405, 418, 429, 503}
CWS_HOSTS = {"chromewebstore.google.com", "chrome.google.com"}
CWS_ID_RE = re.compile(r"/detail(?:/[^/]+)?/([a-p]{32})")
LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")


def read_links(path: str) -> list[str]:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    return sorted({m.group(1).rstrip(".,;") for m in LINK_RE.finditer(text)})


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Return 3xx responses instead of following them."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D102
        return None


def _request(url: str, timeout: float, follow: bool) -> tuple[int | None, str]:
    ctx = ssl.create_default_context()
    handlers = [urllib.request.HTTPSHandler(context=ctx)]
    if not follow:
        handlers.append(_NoRedirect())
    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(
        url,
        method="GET",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    try:
        with opener.open(req, timeout=timeout) as resp:
            return resp.status, ""
    except urllib.error.HTTPError as err:
        return err.code, err.reason or ""
    except urllib.error.URLError as err:
        return None, str(getattr(err, "reason", err))
    except (socket.timeout, TimeoutError):
        return None, "timeout"
    except Exception as err:  # noqa: BLE001 - report, never crash
        return None, f"{type(err).__name__}: {err}"


def check_webstore(url: str, timeout: float) -> tuple[str, int | None, str]:
    """Return (state, status, detail) for a Chrome Web Store URL."""
    match = CWS_ID_RE.search(url)
    if not match:
        status, detail = _request(url, timeout, follow=True)
        if status and status < 400:
            return "ok", status, ""
        return ("broken" if status and status >= 400 else "broken"), status, detail or "invalid store URL"

    ext_id = match.group(1)
    probe = (
        "https://clients2.google.com/service/update2/crx"
        "?response=redirect&prodversion=130.0&acceptformat=crx2,crx3"
        f"&x=id%3D{ext_id}%26uc"
    )
    status, detail = _request(probe, timeout, follow=False)
    if status in (301, 302, 303, 307, 308):
        return "ok", status, ""
    if status in (204, 200):
        # No update offered but the item is known to the service.
        return "ok", status, ""
    if status == 404:
        return "broken", status, "removed from the store (unavailable)"
    if status in WARN_STATUSES:
        return "warn", status, detail
    if status is None:
        return "error", None, detail
    return "broken", status, detail


def check_url(url: str, timeout: float, retries: int = 2) -> dict:
    host = urllib.parse.urlsplit(url).netloc.lower()
    if host in CWS_HOSTS:
        state, status, detail = check_webstore(url, timeout)
    else:
        state, status, detail = "error", None, "unreachable"
        for attempt in range(retries + 1):
            status, detail = _request(url, timeout, follow=True)
            if status is None:
                state = "error"
                continue
            if status < 400:
                state = "ok"
            elif status in WARN_STATUSES:
                state = "warn"
            else:
                state = "broken"
            break
    return {"url": url, "state": state, "status": status, "detail": detail}


def main() -> int:
    parser = argparse.ArgumentParser(description="Check links in README.md")
    parser.add_argument("--file", default=README)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--json", dest="json_path")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"error: {args.file} not found", file=sys.stderr)
        return 2

    links = read_links(args.file)
    print(f"Checking {len(links)} unique links from {args.file} ...\n", flush=True)

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(check_url, url, args.timeout, args.retries): url for url in links
        }
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    order = {"broken": 0, "error": 1, "warn": 2, "ok": 3}
    results.sort(key=lambda r: (order[r["state"]], r["url"]))

    broken = [r for r in results if r["state"] in ("broken", "error")]
    warned = [r for r in results if r["state"] == "warn"]

    if broken:
        print("BROKEN LINKS\n")
        for r in broken:
            status = r["status"] if r["status"] is not None else "no response"
            print(f"  [{status}] {r['url']}")
            if r["detail"]:
                print(f"          {r['detail']}")
        print()

    if warned:
        print("WARNINGS (likely bot protection, verify manually)\n")
        for r in warned:
            print(f"  [{r['status']}] {r['url']}")
        print()

    ok = len(results) - len(broken) - len(warned)
    print(f"Summary: {len(results)} links checked, {ok} ok, {len(warned)} warnings, {len(broken)} broken")

    if args.json_path:
        with open(args.json_path, "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=2)
        print(f"JSON report written to {args.json_path}")

    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
