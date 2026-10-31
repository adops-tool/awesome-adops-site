[![Awesome AdOps](https://github.com/adops-tool/awesome-adops-site/blob/main/image/awesome-adops-site_1.png)](https://github.com/adops-tool/awesome-adops-site)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

# Awesome AdOps

A curated directory of practical resources for advertising operations (AdOps), ad technology, programmatic media, and publisher monetization. It prioritizes authoritative documentation, useful tools, and clearly relevant projects.

> **Note:** Ad-tech changes quickly. Products, endpoints, and ownership can change; check the linked source for current availability. Inclusion is not an endorsement. The directory is organized by a resource’s primary use; a few tools may overlap categories.

## Contents

- [Standards, Trade Bodies & Specifications](#standards-trade-bodies--specifications)
- [Header Bidding & Prebid](#header-bidding--prebid)
- [Ad Serving, Publisher Platforms & Monetization](#ad-serving-publisher-platforms--monetization)
- [Demand-Side Platforms & Buying](#demand-side-platforms--buying)
- [Native & Content Advertising](#native--content-advertising)
- [Supply-Side Platforms, Exchanges & Publisher Yield](#supply-side-platforms-exchanges--publisher-yield)
- [Retail Media & Commerce Advertising](#retail-media--commerce-advertising)
- [Video, CTV, Audio & Rich Media](#video-ctv-audio--rich-media)
- [Ads.txt, App-ads.txt, Sellers.json & Supply Chain](#adstxt-app-adstxt-sellersjson--supply-chain)
- [Privacy, Consent & Identity](#privacy-consent--identity)
- [Ad Quality, Verification & Fraud Prevention](#ad-quality-verification--fraud-prevention)
- [Analytics, Attribution & Marketing Data](#analytics-attribution--marketing-data)
- [Ad Operations, Workflow & Sales](#ad-operations-workflow--sales)
- [Creative, Tags & Campaign Utilities](#creative-tags--campaign-utilities)
- [Browser Extensions & AdOps Debugging](#browser-extensions--adops-debugging)
- [Developer Tooling & Testing](#developer-tooling--testing)
- [Open-Source Ad Servers, RTB & Publisher Engineering](#open-source-ad-servers-rtb--publisher-engineering)
- [Mobile Advertising, App Monetization & Gaming](#mobile-advertising-app-monetization--gaming)
- [Ad-Tech Research & Site Discovery](#ad-tech-research--site-discovery)
- [Privacy Sandbox: Retired APIs & Current Status](#privacy-sandbox-retired-apis--current-status)
- [Learning, News & Communities](#learning-news--communities)

## Standards, Trade Bodies & Specifications

- ![Standards](image/dot_1.gif) [AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM) - Advertising Common Object Model.
- ![Standards](image/dot_2.gif) [Ads.txt crawler](https://github.com/InteractiveAdvertisingBureau/ads-txt-crawler) - Crawler for ads.txt and related files.
- ![Standards](image/dot_3.gif) [CATS](https://github.com/InteractiveAdvertisingBureau/CATS) - Content Taxonomy and related classification resources.
- ![Standards](image/dot_4.gif) [Consent String SDK Java](https://github.com/InteractiveAdvertisingBureau/Consent-String-SDK-Java) - Consent-string utilities for Java.
- ![Standards](image/dot_5.gif) [Consent String SDK JS](https://github.com/InteractiveAdvertisingBureau/Consent-String-SDK-JS) - TCF consent-string utilities for JavaScript.
- ![Standards](image/dot_1.gif) [Global Privacy Platform](https://github.com/InteractiveAdvertisingBureau/Global-Privacy-Platform) - Framework for communicating privacy signals.
- ![Standards](image/dot_2.gif) [IAB](https://www.iab.com/) - Digital advertising industry association.
- ![Standards](image/dot_3.gif) [IAB Europe](https://iabeurope.eu/) - European digital advertising association.
- ![Standards](image/dot_4.gif) [IAB TCF JavaScript SDK](https://github.com/InteractiveAdvertisingBureau/iabtcf-es) - JavaScript implementation of TCF APIs.
- ![Standards](image/dot_5.gif) [IAB Tech Lab](https://iabtechlab.com/) - Technical standards and tools for digital advertising.
- ![Standards](image/dot_1.gif) [IAB Tech Lab Compliance](https://compliance.iabtechlab.com/) - Compliance resources for industry specifications.
- ![Standards](image/dot_2.gif) [IAB Tech Lab GPP](https://iabtechlab.com/standards/gpp/) - Global Privacy Platform overview and resources.
- ![Standards](image/dot_3.gif) [IAB Tech Lab Tools](https://tools.iabtechlab.com/) - Validators and utilities for advertising standards.
- ![Standards](image/dot_4.gif) [MRAID](https://github.com/InteractiveAdvertisingBureau/MRAID) - Mobile Rich Media Ad Interface Definitions.
- ![Standards](image/dot_5.gif) [Open Measurement JS Clients](https://github.com/InteractiveAdvertisingBureau/Open-Measurement-JSClients) - JavaScript OM SDK clients.
- ![Standards](image/dot_1.gif) [Open Measurement SDK](https://iabtechlab.com/standards/open-measurement-sdk/) - Open measurement standard for ad verification.
- ![Standards](image/dot_2.gif) [OpenRTB](https://iabtechlab.com/standards/openrtb/) - Real-time bidding protocol and specifications.
- ![Standards](image/dot_3.gif) [OpenRTB 2.x](https://github.com/InteractiveAdvertisingBureau/openrtb2.x) - OpenRTB version 2.x materials.
- ![Standards](image/dot_4.gif) [OpenRTB documentation](https://openrtb.github.io/OpenRTB/) - Browsable OpenRTB specification.
- ![Standards](image/dot_5.gif) [OpenRTB GitHub specification](https://github.com/InteractiveAdvertisingBureau/openrtb) - OpenRTB source and documentation.
- ![Standards](image/dot_1.gif) [SafeFrame](https://github.com/InteractiveAdvertisingBureau/SafeFrame) - Secure ad iframe API specification.
- ![Standards](image/dot_2.gif) [Seller Domain Verification](https://github.com/InteractiveAdvertisingBureau/Seller-Domain-Verification) - Seller domain verification resources.
- ![Standards](image/dot_3.gif) [Seller-Defined Audiences](https://github.com/InteractiveAdvertisingBureau/Seller-Defined-Audiences) - Standards for publisher-defined audience signals.
- ![Standards](image/dot_4.gif) [SIMID](https://github.com/InteractiveAdvertisingBureau/SIMID) - Secure Interactive Media Interface Definition.
- ![Standards](image/dot_5.gif) [Supply Chain Validation](https://github.com/InteractiveAdvertisingBureau/Supply-Chain-Validation) - Validation resources for the SupplyChain object.
- ![Standards](image/dot_1.gif) [TCF GitHub](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework) - TCF specifications and resources.
- ![Standards](image/dot_2.gif) [TCF resources](https://iabeurope.eu/tcf-supporting-resources/) - IAB Europe Transparency & Consent Framework materials.
- ![Standards](image/dot_3.gif) [US Privacy](https://github.com/InteractiveAdvertisingBureau/USPrivacy) - US privacy specification resources.
- ![Standards](image/dot_4.gif) [VAST](https://iabtechlab.com/standards/vast/) - Video Ad Serving Template specification.
- ![Standards](image/dot_5.gif) [VAST 4.x](https://github.com/InteractiveAdvertisingBureau/VAST4.x) - VAST 4.x resources.
- ![Standards](image/dot_1.gif) [VAST GitHub](https://github.com/InteractiveAdvertisingBureau/VAST) - VAST specification source.
- ![Standards](image/dot_2.gif) [VAST Samples](https://github.com/InteractiveAdvertisingBureau/VAST-Samples) - Example VAST tags and creatives.
- ![Standards](image/dot_3.gif) [VMAP](https://github.com/InteractiveAdvertisingBureau/VMAP) - Video Multiple Ad Playlist specification.

## Header Bidding & Prebid

- ![Header Bidding](image/dot_1.gif) [Bidder adapter guide](https://docs.prebid.org/dev-docs/bidder-adaptor.html) - Implementing a Prebid.js bidder adapter.
- ![Header Bidding](image/dot_2.gif) [HeaderBid Expert](https://github.com/prebid/headerbid-expert) - Prebid-related browser debugging project.
- ![Header Bidding](image/dot_3.gif) [Prebid Ad Ops](https://adops.dev/adtech) - Ad-tech learning resources and practical guides.
- ![Header Bidding](image/dot_4.gif) [Prebid currency file](https://github.com/prebid/currency-file) - Currency rates used by Prebid.js.
- ![Header Bidding](image/dot_5.gif) [Prebid debugging guide](https://docs.prebid.org/debugging/debugging.html) - Troubleshooting common Prebid integrations.
- ![Header Bidding](image/dot_1.gif) [Prebid documentation](https://docs.prebid.org/) - Documentation for Prebid products and integrations.
- ![Header Bidding](image/dot_2.gif) [Prebid downloads](https://docs.prebid.org/Download.html) - Build and download Prebid.js bundles.
- ![Header Bidding](image/dot_3.gif) [Prebid external JS template](https://github.com/prebid/prebid-js-external-js-template) - Template for external Prebid.js modules.
- ![Header Bidding](image/dot_4.gif) [Prebid Mobile Android](https://github.com/prebid/prebid-mobile-android) - Prebid Mobile SDK for Android.
- ![Header Bidding](image/dot_5.gif) [Prebid Mobile iOS](https://github.com/prebid/prebid-mobile-ios) - Prebid Mobile SDK for iOS.
- ![Header Bidding](image/dot_1.gif) [Prebid Sales Agent](https://github.com/prebid/salesagent) - Prebid sales-agent project.
- ![Header Bidding](image/dot_2.gif) [Prebid Server](https://github.com/prebid/prebid-server) - Open-source server-side header bidding solution.
- ![Header Bidding](image/dot_3.gif) [Prebid Server bidders](https://docs.prebid.org/dev-docs/pbs-bidders.html) - Prebid Server adapter documentation.
- ![Header Bidding](image/dot_4.gif) [Prebid Server Java](https://github.com/prebid/prebid-server-java) - Java implementation of Prebid Server.
- ![Header Bidding](image/dot_5.gif) [Prebid tools](https://docs.prebid.org/tools/) - Debugging and implementation tools.
- ![Header Bidding](image/dot_1.gif) [Prebid Universal Creative](https://github.com/prebid/prebid-universal-creative) - Universal creative for rendering Prebid ad responses.
- ![Header Bidding](image/dot_2.gif) [Prebid.js](https://github.com/prebid/Prebid.js) - Open-source header bidding wrapper for web publishers.
- ![Header Bidding](image/dot_3.gif) [Prebid.js reference](https://docs.prebid.org/dev-docs/publisher-api-reference.html) - Publisher API documentation.
- ![Header Bidding](image/dot_4.gif) [Prebid.org](https://prebid.org/) - Prebid community, projects, and ecosystem.
- ![Header Bidding](image/dot_5.gif) [Professor Prebid](https://github.com/prebid/professor-prebid) - Browser extension for inspecting Prebid auctions.
- ![Header Bidding](image/dot_1.gif) [Professor Prebid extension](https://chromewebstore.google.com/detail/professor-prebid/kdnllijdimhbledmfdbljampcdphcbdc) - Chrome DevTools panel for Prebid debugging.

## Ad Serving, Publisher Platforms & Monetization

- ![Ad Serving](image/dot_1.gif) [AdButler](https://www.adbutler.com/) - Ad serving and campaign management.
- ![Ad Serving](image/dot_2.gif) [AdGlare](https://www.adglare.com/) - Ad serving and campaign management.
- ![Ad Serving](image/dot_3.gif) [AdSpeed](https://www.adspeed.com/) - Ad serving and ad management.
- ![Ad Serving](image/dot_4.gif) [AdvertServe](https://www.advertserve.com/) - Ad serving for publishers and agencies.
- ![Ad Serving](image/dot_5.gif) [Broadstreet](https://broadstreetads.com/) - Ad management for local publishers and media groups.
- ![Ad Serving](image/dot_1.gif) [EPOM](https://epom.com/) - Ad server and ad-tech platform.
- ![Ad Serving](image/dot_2.gif) [Equativ](https://equativ.com/) - Ad-tech and media platform.
- ![Ad Serving](image/dot_3.gif) [Google Ad Manager](https://admanager.google.com/) - Ad serving, campaign management, and monetization platform.
- ![Ad Serving](image/dot_4.gif) [Google Ad Manager API](https://developers.google.com/ad-manager/api/start) - API documentation and getting-started material.
- ![Ad Serving](image/dot_5.gif) [Google AdSense](https://www.google.com/adsense/) - Publisher advertising and monetization.
- ![Ad Serving](image/dot_1.gif) [Google Publisher Tag](https://developers.google.com/publisher-tag) - JavaScript library and documentation for publisher ad requests and inventory.
- ![Ad Serving](image/dot_2.gif) [GPT reference](https://developers.google.com/publisher-tag/reference) - Google Publisher Tag API reference.
- ![Ad Serving](image/dot_3.gif) [GPT samples](https://developers.google.com/publisher-tag/samples) - Publisher Tag implementation examples.
- ![Ad Serving](image/dot_4.gif) [Revive Adserver](https://www.revive-adserver.com/) - Open-source ad serving platform.
- ![Ad Serving](image/dot_5.gif) [Revive Adserver GitHub](https://github.com/revive-adserver/revive-adserver) - Source code for Revive Adserver.

## Demand-Side Platforms & Buying

- ![DSP](image/dot_1.gif) [AdRoll](https://www.adroll.com/) - Cross-channel advertising and retargeting.
- ![DSP](image/dot_2.gif) [Amazon Ads](https://advertising.amazon.com/) - Advertising products and demand-side buying from Amazon.
- ![DSP](image/dot_3.gif) [Basis](https://www.basis.com/) - Programmatic media and campaign management platform.
- ![DSP](image/dot_4.gif) [Beeswax](https://www.beeswax.com/) - Bidder-as-a-Service and programmatic infrastructure.
- ![DSP](image/dot_5.gif) [Choozle](https://www.choozle.com/) - Self-service programmatic advertising platform.
- ![DSP](image/dot_1.gif) [Cognitiv](https://www.cognitiv.ai/) - Deep-learning programmatic advertising.
- ![DSP](image/dot_2.gif) [DeepIntent](https://www.deepintent.com/) - Healthcare-focused programmatic advertising.
- ![DSP](image/dot_3.gif) [Display & Video 360](https://marketingplatform.google.com/about/display-video-360/) - Google's programmatic buying and campaign management platform.
- ![DSP](image/dot_4.gif) [Eskimi](https://www.eskimi.com/) - Programmatic advertising and audience platform.
- ![DSP](image/dot_5.gif) [Google Ads](https://ads.google.com/ups/routing?source=206&subid=xs-ip-gemini-adlt) - Google’s advertiser platform for creating and managing campaigns.
- ![DSP](image/dot_1.gif) [Jampp](https://www.jampp.com/) - Mobile app growth and programmatic advertising.
- ![DSP](image/dot_2.gif) [Kayzen](https://www.kayzen.io/) - Mobile-first programmatic DSP.
- ![DSP](image/dot_3.gif) [Quantcast](https://www.quantcast.com/) - Audience intelligence and programmatic advertising.
- ![DSP](image/dot_4.gif) [Remerge](https://www.remerge.io/) - Mobile app retargeting platform.
- ![DSP](image/dot_5.gif) [RTB House](https://www.rtbhouse.com/) - AI-powered programmatic advertising.
- ![DSP](image/dot_1.gif) [Simpli.fi](https://www.simpli.fi/) - Programmatic advertising and localized marketing.
- ![DSP](image/dot_2.gif) [Smadex](https://www.smadex.com/) - Mobile programmatic advertising platform.
- ![DSP](image/dot_3.gif) [StackAdapt](https://www.stackadapt.com/) - Multi-channel programmatic advertising platform.
- ![DSP](image/dot_4.gif) [The Trade Desk](https://www.thetradedesk.com/) - Independent programmatic advertising platform.
- ![DSP](image/dot_5.gif) [Viant](https://www.viantinc.com/) - Demand-side platform and advertising technology.
- ![DSP](image/dot_1.gif) [Yahoo Advertising](https://www.yahooinc.com/advertising/) - Media, data, and advertising platform.

## Native & Content Advertising

- ![Native Ads](image/dot_1.gif) [Dianomi](https://www.dianomi.com/) - Native advertising for financial and business publishers.
- ![Native Ads](image/dot_2.gif) [MGID](https://mgid.com/) - Native advertising platform.
- ![Native Ads](image/dot_3.gif) [Outbrain](https://www.outbrain.com/) - Content recommendation and native advertising.
- ![Native Ads](image/dot_4.gif) [Plista](https://www.plista.com/) - Native advertising and content recommendation.
- ![Native Ads](image/dot_5.gif) [Revcontent](https://revcontent.com/) - Content recommendation and native advertising.
- ![Native Ads](image/dot_1.gif) [Taboola](https://www.taboola.com/) - Content discovery and performance advertising.
- ![Native Ads](image/dot_2.gif) [Zemanta](https://www.zemanta.com/) - Native advertising and programmatic campaign platform.

## Supply-Side Platforms, Exchanges & Publisher Yield

- ![SSP & Yield](image/dot_1.gif) [33Across](https://www.33across.com/) - Supply-side platform and identity technology.
- ![SSP & Yield](image/dot_2.gif) [Adagio](https://www.adagio.io/) - Publisher monetization and advertising platform.
- ![SSP & Yield](image/dot_3.gif) [Adapex](https://www.adapex.io/) - Publisher monetization and ad operations.
- ![SSP & Yield](image/dot_4.gif) [Aditude](https://www.aditude.io/) - Publisher monetization and advertising technology.
- ![SSP & Yield](image/dot_5.gif) [AdMixer](https://www.admixer.com/) - Ad-tech platform including retail and digital media solutions.
- ![SSP & Yield](image/dot_1.gif) [AdPushup](https://www.adpushup.com/) - Ad revenue optimization for publishers.
- ![SSP & Yield](image/dot_2.gif) [Adtelligent](https://www.adtelligent.com/) - Advertising technology and monetization platform.
- ![SSP & Yield](image/dot_3.gif) [Amazon Publisher Services](https://aps.amazon.com/) - Publisher services and transparent advertising marketplace.
- ![SSP & Yield](image/dot_4.gif) [Assertive Yield](https://www.assertiveyield.com/) - Yield management for publishers.
- ![SSP & Yield](image/dot_5.gif) [Automatad](https://www.automatad.com/) - Publisher ad monetization and optimization platform.
- ![SSP & Yield](image/dot_1.gif) [Azerion](https://www.azerion.com/) - Digital advertising and entertainment platform.
- ![SSP & Yield](image/dot_2.gif) [Browsi](https://www.browsi.com/) - Publisher optimization and monetization technology.
- ![SSP & Yield](image/dot_3.gif) [Ezoic](https://www.ezoic.com/) - Publisher monetization and site optimization platform.
- ![SSP & Yield](image/dot_4.gif) [Freestar](https://www.freestar.com/) - Publisher monetization and ad operations.
- ![SSP & Yield](image/dot_5.gif) [GENIEE](https://www.geniee.co.jp/en/) - Ad-tech, publisher monetization, and marketing solutions.
- ![SSP & Yield](image/dot_1.gif) [Gourmet Ads](https://www.gourmetads.com/) - Food and lifestyle publisher advertising network.
- ![SSP & Yield](image/dot_2.gif) [GumGum](https://gumgum.com/) - Contextual advertising and publisher monetization.
- ![SSP & Yield](image/dot_3.gif) [Hubvisor](https://www.hubvisor.io/) - Publisher monetization and yield management.
- ![SSP & Yield](image/dot_4.gif) [Improve Digital](https://www.improvedigital.com/) - Programmatic advertising and publisher monetization.
- ![SSP & Yield](image/dot_5.gif) [Index Exchange](https://www.indexexchange.com/) - Global advertising exchange.
- ![SSP & Yield](image/dot_1.gif) [Kargo](https://www.kargo.com/) - Mobile and premium publisher advertising.
- ![SSP & Yield](image/dot_2.gif) [Kiosked](https://www.kiosked.com/) - Advertising formats and media monetization technology.
- ![SSP & Yield](image/dot_3.gif) [Magnite](https://www.magnite.com/) - Independent sell-side advertising platform.
- ![SSP & Yield](image/dot_4.gif) [Media.net](https://www.medianet.com/) - Contextual advertising and publisher monetization.
- ![SSP & Yield](image/dot_5.gif) [Mediavine](https://www.mediavine.com/) - Publisher ad management and monetization.
- ![SSP & Yield](image/dot_1.gif) [MonetizeMore](https://www.monetizemore.com/) - Publisher ad optimization and monetization services.
- ![SSP & Yield](image/dot_2.gif) [Nativo](https://www.nativo.com/) - Native advertising platform for brands and publishers.
- ![SSP & Yield](image/dot_3.gif) [Netlink](https://www.netlink.vn/) - Digital publishing and advertising technology.
- ![SSP & Yield](image/dot_4.gif) [NitroPay](https://www.nitropay.com/) - Advertising platform for digital publishers.
- ![SSP & Yield](image/dot_5.gif) [OpenX](https://www.openx.com/) - Programmatic marketplace and supply platform.
- ![SSP & Yield](image/dot_1.gif) [Opti Digital](https://optad360.com/) - Publisher monetization technology.
- ![SSP & Yield](image/dot_2.gif) [Playwire](https://www.playwire.com/) - Publisher monetization platform.
- ![SSP & Yield](image/dot_3.gif) [Proper Media](https://www.proper.io/) - Publisher ad management and monetization services.
- ![SSP & Yield](image/dot_4.gif) [Publift](https://www.publift.com/) - Publisher ad monetization and yield optimization.
- ![SSP & Yield](image/dot_5.gif) [PubMatic](https://pubmatic.com/) - Sell-side platform for digital publishers.
- ![SSP & Yield](image/dot_1.gif) [Pubstack](https://www.pubstack.io/) - Header bidding management and analytics.
- ![SSP & Yield](image/dot_2.gif) [PulsePoint](https://www.pulsepoint.com/) - Programmatic advertising and health media.
- ![SSP & Yield](image/dot_3.gif) [Raptive](https://raptive.com/) - Publisher monetization network.
- ![SSP & Yield](image/dot_4.gif) [Refinery89](https://www.refinery89.com/) - Publisher monetization technology.
- ![SSP & Yield](image/dot_5.gif) [Relevant Digital](https://www.relevant-digital.com/) - Publisher monetization and ad-tech services.
- ![SSP & Yield](image/dot_1.gif) [Seedtag](https://www.seedtag.com/) - Contextual advertising and media solutions.
- ![SSP & Yield](image/dot_2.gif) [Setupad](https://setupad.com/) - Publisher monetization and header bidding.
- ![SSP & Yield](image/dot_3.gif) [Sharethrough](https://www.sharethrough.com/) - Independent omnichannel ad exchange.
- ![SSP & Yield](image/dot_4.gif) [She Media](https://www.shemedia.com/) - Publisher network and advertising solutions.
- ![SSP & Yield](image/dot_5.gif) [Snigel](https://www.snigel.com/) - Publisher ad monetization and header bidding.
- ![SSP & Yield](image/dot_1.gif) [Sonobi](https://www.sonobi.com/) - Publisher-focused advertising technology.
- ![SSP & Yield](image/dot_2.gif) [Sovrn](https://www.sovrn.com/) - Publisher technology and monetization.
- ![SSP & Yield](image/dot_3.gif) [Ströer](https://www.stroeer.de/) - German media and advertising group.
- ![SSP & Yield](image/dot_4.gif) [Teads](https://www.teads.com/) - Global omnichannel advertising platform.
- ![SSP & Yield](image/dot_5.gif) [TripleLift](https://www.triplelift.com/) - SSP focused on native, video, and CTV formats.
- ![SSP & Yield](image/dot_1.gif) [Undertone](https://www.undertone.com/) - Digital advertising and publisher monetization.
- ![SSP & Yield](image/dot_2.gif) [Value Impression](https://www.valueimpression.com/) - Publisher monetization and advertising services.
- ![SSP & Yield](image/dot_3.gif) [Venatus](https://www.venatus.com/) - Gaming and entertainment advertising platform.
- ![SSP & Yield](image/dot_4.gif) [Verve](https://www.verve.com/) - Omnichannel advertising and location technology.
- ![SSP & Yield](image/dot_5.gif) [Xandr](https://xandr.com/) - Digital advertising marketplace and technology.
- ![SSP & Yield](image/dot_1.gif) [Yieldbird](https://www.yieldbird.com/) - Publisher yield optimization.
- ![SSP & Yield](image/dot_2.gif) [Yieldlab](https://www.yieldlab.de/) - Programmatic publisher platform.
- ![SSP & Yield](image/dot_3.gif) [Yieldmo](https://www.yieldmo.com/) - Advertising exchange and creative formats.

## Retail Media & Commerce Advertising

- ![Retail Media](image/dot_1.gif) [AnyMind Group](https://anymindgroup.com/) - Commerce, marketing, and publisher technology.
- ![Retail Media](image/dot_2.gif) [CitrusAd](https://www.citrusad.com/) - Retail media advertising technology.
- ![Retail Media](image/dot_3.gif) [Criteo](https://www.criteo.com/) - Commerce media and advertising technology.
- ![Retail Media](image/dot_4.gif) [Kevel](https://kevel.com/) - Ad serving and retail media infrastructure for commerce businesses.

## Video, CTV, Audio & Rich Media

- ![Video](image/dot_1.gif) [Beachfront](https://www.beachfront.com/) - CTV and video advertising marketplace.
- ![Video](image/dot_2.gif) [Bitmovin Stream Test](https://bitmovin.com/demos/stream-test) - Test video and streaming playback.
- ![Video](image/dot_3.gif) [Connatix](https://www.connatix.com/) - Video technology for publishers and advertisers.
- ![Video](image/dot_4.gif) [dash.js reference player](https://reference.dashif.org/dash.js/) - DASH reference player and test interface.
- ![Video](image/dot_5.gif) [FizzKit VAST Inspector](https://fizzkit.net/tools/vast-inspector/) - Inspect video ad tags.
- ![Video](image/dot_1.gif) [Fluid Player VAST Inspector](https://www.fluidplayer.com/vast-inspector/) - Test VAST tags using Fluid Player.
- ![Video](image/dot_2.gif) [FreeWheel](https://www.freewheel.com/) - Video advertising management and monetization.
- ![Video](image/dot_3.gif) [Google IMA](https://developers.google.com/interactive-media-ads) - Interactive Media Ads SDKs and documentation.
- ![Video](image/dot_4.gif) [Google IMA Flutter](https://github.com/googleads/googleads-mobile-flutter) - Google Mobile Ads Flutter plugin.
- ![Video](image/dot_5.gif) [Google IMA Unity](https://github.com/googleads/googleads-mobile-unity) - Google Mobile Ads Unity plugin.
- ![Video](image/dot_1.gif) [hls.js demo](https://hlsjs.video-dev.org/demo/) - Browser-based HLS playback testing.
- ![Video](image/dot_2.gif) [IMA Android](https://github.com/googleads/googleads-ima-android) - Android video advertising SDK.
- ![Video](image/dot_3.gif) [IMA HTML5 SDK](https://github.com/googleads/googleads-ima-html5) - HTML5 video ad SDK.
- ![Video](image/dot_4.gif) [IMA iOS](https://github.com/googleads/googleads-ima-ios) - iOS video advertising SDK.
- ![Video](image/dot_5.gif) [IMA SDK Video Suite Inspector](https://googleads.github.io/googleads-ima-html5/vsi/) - Inspect and test IMA video ad tags.
- ![Video](image/dot_1.gif) [JW Player Ad Tester](https://www.jwplayer.com/developers/ad-tester/) - Test video advertising integrations.
- ![Video](image/dot_2.gif) [Primis](https://primis.tech/) - Video discovery and monetization platform.
- ![Video](image/dot_3.gif) [Publica](https://getpublica.com/) - CTV ad platform and monetization.
- ![Video](image/dot_4.gif) [Radiant Media Player VAST Inspector](https://www.radiantmediaplayer.com/vast-inspector.html) - Inspect VAST ad responses.
- ![Video](image/dot_5.gif) [Shaka Player demo](https://shaka-player-demo.appspot.com/) - Demo and test suite for Shaka Player.
- ![Video](image/dot_1.gif) [SpringServe](https://www.springserve.com/) - Video ad serving and monetization.
- ![Video](image/dot_2.gif) [SpringServe VAST tester](https://springserve.com/vast-tag-tester/) - Test VAST tags in a video player.
- ![Video](image/dot_3.gif) [Targetspot](https://www.targetspot.com/) - Digital audio advertising platform.
- ![Video](image/dot_4.gif) [THEOplayer stream tester](https://demo.theoplayer.com/test-your-stream-with-statistics) - Test streams and inspect playback statistics.
- ![Video](image/dot_5.gif) [Triton Digital](https://www.tritondigital.com/) - Audio streaming, podcasting, and advertising technology.
- ![Video](image/dot_1.gif) [VAST Client JS](https://github.com/dailymotion/vast-client-js) - JavaScript VAST client library.
- ![Video](image/dot_2.gif) [VAST Parser](https://github.com/dailymotion/vast-parser) - VAST XML parser for JavaScript.
- ![Video](image/dot_3.gif) [VAST tag validator](https://www.ottengine.com/tools/vast-tag-validator) - Online VAST tag validation.
- ![Video](image/dot_4.gif) [VDO.AI](https://www.vdo.ai/) - Video advertising and publisher monetization.
- ![Video](image/dot_5.gif) [Video.js](https://videojs.com/) - Open-source HTML5 video player.
- ![Video](image/dot_1.gif) [Video.js VAST/VPAID](https://github.com/mailonline/videojs-vast-vpaid) - Video.js plugin for VAST and VPAID ads.

## Ads.txt, App-ads.txt, Sellers.json & Supply Chain

- ![Supply Chain](image/dot_1.gif) [10up Ads.txt](https://github.com/10up/ads-txt) - WordPress ads.txt management plugin.
- ![Supply Chain](image/dot_2.gif) [Ads.txt](https://iabtechlab.com/ads-txt/) - IAB Tech Lab overview and specification resources.
- ![Supply Chain](image/dot_3.gif) [Ads.txt and app-ads.txt validator](https://github.com/adops-tool/Validate-and-Optimize-app-ads.txt-ads.txt-file) - Validate and optimize ads.txt files.
- ![Supply Chain](image/dot_4.gif) [Ads.txt Guru](https://adstxt.guru/) - Ads.txt inspection and management resources.
- ![Supply Chain](image/dot_5.gif) [Ads.txt Manager](https://www.adstxtmanager.com/) - Manage and maintain ads.txt files.
- ![Supply Chain](image/dot_1.gif) [Ads.txt matcher](https://github.com/adops-tool/Matcher-ads.txt-app-ads.txt) - Compare and match ads.txt and app-ads.txt entries.
- ![Supply Chain](image/dot_2.gif) [Ads.txt Validator](https://www.adstxtvalidator.com/) - Validate ads.txt files.
- ![Supply Chain](image/dot_3.gif) [AdVerify crawler](https://github.com/adops-tool/AdVerify-adstxt-appadstxt-Crawler) - Crawl ads.txt and app-ads.txt files.
- ![Supply Chain](image/dot_4.gif) [App-ads.txt](https://app-ads-txt.com/) - App-ads.txt lookup and resources.
- ![Supply Chain](image/dot_5.gif) [FIZZ Ads.txt Validator](https://fizzkit.net/tools/adstxt-validator/) - Validate ads.txt entries.
- ![Supply Chain](image/dot_1.gif) [Sellers.guide](https://sellers.guide/) - Sellers.json and supply chain transparency tools.
- ![Supply Chain](image/dot_2.gif) [Sellers.json](https://iabtechlab.com/sellers-json/) - Seller transparency specification resources.
- ![Supply Chain](image/dot_3.gif) [SellersJSON.com](https://sellersjson.com/) - Sellers.json lookup and validation.
- ![Supply Chain](image/dot_4.gif) [Well-known.dev](https://well-known.dev/) - Explore well-known files and web identity resources.

## Privacy, Consent & Identity

- ![Privacy](image/dot_1.gif) [ATS.js](https://github.com/LiveRamp/ats.js) - LiveRamp ATS JavaScript integration.
- ![Privacy](image/dot_2.gif) [CHIPS](https://privacysandbox.google.com/cookies/chips) - Partitioned cookies for embedded content across sites.
- ![Privacy](image/dot_3.gif) [Consent String Decoder](https://www.consentstringdecoder.com/) - Decode IAB TCF consent strings.
- ![Privacy](image/dot_4.gif) [Cookiebot](https://www.cookiebot.com/) - Cookie consent and compliance solution.
- ![Privacy](image/dot_5.gif) [CookieConsent](https://github.com/orestbida/cookieconsent) - Lightweight cookie consent manager.
- ![Privacy](image/dot_1.gif) [CookieYes](https://www.cookieyes.com/) - Cookie consent and privacy compliance.
- ![Privacy](image/dot_2.gif) [Didomi](https://www.didomi.io/) - Consent and preference management platform.
- ![Privacy](image/dot_3.gif) [Didomi Consent](https://github.com/Didomi/consent) - Consent SDK and open-source resources.
- ![Privacy](image/dot_4.gif) [FedCM](https://privacysandbox.google.com/cookies/fedcm) - Browser API for federated identity flows.
- ![Privacy](image/dot_5.gif) [Funding Choices](https://fundingchoices.google.com/) - Google publisher consent and funding tools.
- ![Privacy](image/dot_1.gif) [Habu](https://www.habu.com/) - Data clean room technology.
- ![Privacy](image/dot_2.gif) [IAB TCF](https://iabtcf.com/) - Community resources and consent-string tools.
- ![Privacy](image/dot_3.gif) [ID5](https://www.id5.io/) - Identity solution for digital advertising.
- ![Privacy](image/dot_4.gif) [ID5 API JS](https://github.com/id5io/id5-api.js) - JavaScript client for ID5 APIs.
- ![Privacy](image/dot_5.gif) [InfoSum](https://www.infosum.com/) - Privacy-safe data collaboration.
- ![Privacy](image/dot_1.gif) [iubenda](https://www.iubenda.com/) - Privacy compliance and consent tools.
- ![Privacy](image/dot_2.gif) [Ketch](https://www.ketch.com/) - Privacy and data governance platform.
- ![Privacy](image/dot_3.gif) [Klaro](https://github.com/kiprotect/klaro) - Open-source consent management solution.
- ![Privacy](image/dot_4.gif) [LiveRamp ATS](https://liveramp.com/) - Identity and data collaboration technology.
- ![Privacy](image/dot_5.gif) [Lotame](https://www.lotame.com/) - Data and identity solutions.
- ![Privacy](image/dot_1.gif) [OneTrust](https://www.onetrust.com/) - Privacy, consent, and governance platform.
- ![Privacy](image/dot_2.gif) [Osano](https://www.osano.com/) - Privacy management and consent solution.
- ![Privacy](image/dot_3.gif) [Permutive](https://www.permutive.com/) - Publisher data and audience platform.
- ![Privacy](image/dot_4.gif) [Private State Tokens](https://privacysandbox.google.com/protections/private-state-tokens) - Privacy-preserving tokens intended to help combat fraud and abuse.
- ![Privacy](image/dot_5.gif) [Quantcast Choice](https://www.quantcast.com/products/choice-consent-management-platform/) - Consent management platform.
- ![Privacy](image/dot_1.gif) [Snowflake](https://www.snowflake.com/) - Cloud data platform with data collaboration capabilities.
- ![Privacy](image/dot_2.gif) [Sourcepoint](https://www.sourcepoint.com/) - Privacy consent and publisher monetization solutions.
- ![Privacy](image/dot_3.gif) [TCF Global Vendor List](https://vendor-list.consensu.org/v3/vendor-list.json) - Official TCF vendor-list JSON endpoint.
- ![Privacy](image/dot_4.gif) [TCF Vendor List](https://www.tcfvendorlist.com/) - Browse registered TCF vendors.
- ![Privacy](image/dot_5.gif) [Transcend](https://transcend.io/) - Privacy infrastructure and data rights management.
- ![Privacy](image/dot_1.gif) [TransUnion](https://www.transunion.com/) - Identity and audience data solutions.
- ![Privacy](image/dot_2.gif) [UID2 Core](https://github.com/UnifiedID2/uid2-core) - Core UID2 libraries.
- ![Privacy](image/dot_3.gif) [UID2 Operator](https://github.com/UnifiedID2/uid2-operator) - UID2 operator implementation.
- ![Privacy](image/dot_4.gif) [UID2 web integrations](https://github.com/UnifiedID2/uid2-web-integrations) - Browser-side UID2 integration examples.
- ![Privacy](image/dot_5.gif) [UniConsent](https://www.uniconsent.com/) - Consent management for publishers.
- ![Privacy](image/dot_1.gif) [Unified ID 2.0](https://unifiedid.com/) - Industry identity framework and documentation.
- ![Privacy](image/dot_2.gif) [Usercentrics](https://www.usercentrics.com/) - Consent management platform.

## Ad Quality, Verification & Fraud Prevention

- ![Verification](image/dot_1.gif) [Ad Lightning](https://www.adlightning.com/) - Ad quality and creative scanning.
- ![Verification](image/dot_2.gif) [Ad verification guidelines](https://github.com/InteractiveAdvertisingBureau/Ad-Verification-Guidelines) - IAB guidelines for ad verification.
- ![Verification](image/dot_3.gif) [AdSecure](https://www.adsecure.com/) - Ad quality scanning and creative verification.
- ![Verification](image/dot_4.gif) [Anura](https://www.anura.io/) - Ad fraud detection and traffic quality analysis.
- ![Verification](image/dot_5.gif) [AppsFlyer Protect360](https://www.appsflyer.com/products/protect360/) - Mobile ad fraud protection.
- ![Verification](image/dot_1.gif) [Check My Ads](https://checkmyads.org/) - Community initiative for responsible digital advertising.
- ![Verification](image/dot_2.gif) [CHEQ](https://cheq.ai/) - Go-to-market security and invalid traffic protection.
- ![Verification](image/dot_3.gif) [Clean.io](https://www.clean.io/) - Malvertising and ad quality protection.
- ![Verification](image/dot_4.gif) [ClickCease](https://www.clickcease.com/) - Click fraud protection for paid campaigns.
- ![Verification](image/dot_5.gif) [Confiant](https://www.confiant.com/) - Client-side ad security and quality monitoring.
- ![Verification](image/dot_1.gif) [DoubleVerify](https://doubleverify.com/) - Media quality, verification, and measurement.
- ![Verification](image/dot_2.gif) [GeoEdge](https://www.geoedge.com/) - Ad quality and malvertising protection.
- ![Verification](image/dot_3.gif) [Human Security](https://www.humansecurity.com/) - Bot mitigation and digital fraud protection.
- ![Verification](image/dot_4.gif) [Integral Ad Science](https://integralads.com/) - Viewability, brand safety, and ad fraud measurement.
- ![Verification](image/dot_5.gif) [MFilterIt](https://www.mfilterit.com/) - Digital ad fraud and brand safety tools.
- ![Verification](image/dot_1.gif) [Pixalate](https://www.pixalate.com/) - Ad fraud, privacy, and compliance analytics.
- ![Verification](image/dot_2.gif) [Protected Media](https://www.protected.media/) - Invalid traffic detection and ad verification.
- ![Verification](image/dot_3.gif) [Scalarr](https://www.scalarr.io/) - Mobile advertising fraud prevention.
- ![Verification](image/dot_4.gif) [Spider AF](https://www.spideraf.com/) - Ad fraud detection and prevention.
- ![Verification](image/dot_5.gif) [TrafficGuard](https://www.trafficguard.ai/) - Invalid traffic detection and prevention.

## Analytics, Attribution & Marketing Data

- ![Analytics](image/dot_1.gif) [Adjust](https://www.adjust.com/) - Mobile measurement, attribution, and analytics.
- ![Analytics](image/dot_2.gif) [Adverity](https://www.adverity.com/) - Marketing data integration and analytics.
- ![Analytics](image/dot_3.gif) [Airbridge](https://www.airbridge.io/) - Mobile measurement and growth analytics.
- ![Analytics](image/dot_4.gif) [Apache Superset](https://superset.apache.org/) - Open-source data exploration and visualization.
- ![Analytics](image/dot_5.gif) [AppsFlyer](https://www.appsflyer.com/) - Mobile measurement and attribution platform.
- ![Analytics](image/dot_1.gif) [Binom](https://binom.org/) - Self-hosted campaign tracking software.
- ![Analytics](image/dot_2.gif) [Branch](https://www.branch.io/) - Deep linking and mobile measurement.
- ![Analytics](image/dot_3.gif) [Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/) - Build tagged campaign URLs.
- ![Analytics](image/dot_4.gif) [Chartbeat](https://www.chartbeat.com/) - Real-time audience analytics for publishers.
- ![Analytics](image/dot_5.gif) [Databox](https://www.databox.com/) - Business dashboards and performance analytics.
- ![Analytics](image/dot_1.gif) [Everflow](https://www.everflow.io/) - Partner and performance marketing platform.
- ![Analytics](image/dot_2.gif) [Firebase](https://firebase.google.com/) - App analytics, engagement, and development tools.
- ![Analytics](image/dot_3.gif) [Funnel](https://funnel.io/) - Marketing data collection and reporting.
- ![Analytics](image/dot_4.gif) [Google Analytics](https://analytics.google.com/) - Web and app analytics.
- ![Analytics](image/dot_5.gif) [Google Analytics Dev Tools](https://ga-dev-tools.google/) - Utilities for Google Analytics implementations.
- ![Analytics](image/dot_1.gif) [Google Search Console](https://search.google.com/search-console) - Search performance and site diagnostics.
- ![Analytics](image/dot_2.gif) [Google Tag Manager](https://tagmanager.google.com/) - Tag deployment and management.
- ![Analytics](image/dot_3.gif) [Grafana](https://grafana.com/) - Observability dashboards and analytics.
- ![Analytics](image/dot_4.gif) [Impact.com](https://impact.com/) - Partnership management and performance marketing.
- ![Analytics](image/dot_5.gif) [Improvado](https://www.improvado.io/) - Marketing data pipeline and analytics.
- ![Analytics](image/dot_1.gif) [Keitaro](https://keitaro.io/) - Campaign tracking and traffic distribution.
- ![Analytics](image/dot_2.gif) [Kochava](https://kochava.com/) - Mobile attribution and measurement.
- ![Analytics](image/dot_3.gif) [Looker Studio](https://lookerstudio.google.com/) - Reporting and data visualization.
- ![Analytics](image/dot_4.gif) [Marfeel](https://www.marfeel.com/) - Publisher audience, analytics, and monetization tools.
- ![Analytics](image/dot_5.gif) [Metabase](https://www.metabase.com/) - Open-source business intelligence.
- ![Analytics](image/dot_1.gif) [NinjaCat](https://www.ninjacat.io/) - Marketing analytics and reporting.
- ![Analytics](image/dot_2.gif) [Northbeam](https://www.northbeam.io/) - Marketing measurement and attribution analytics.
- ![Analytics](image/dot_3.gif) [Parse.ly](https://www.parsely.com/) - Content analytics and audience intelligence.
- ![Analytics](image/dot_4.gif) [Partnerize](https://www.partnerize.com/) - Partnership automation and affiliate marketing.
- ![Analytics](image/dot_5.gif) [Power BI](https://powerbi.microsoft.com/) - Business intelligence and reporting.
- ![Analytics](image/dot_1.gif) [RedTrack](https://redtrack.io/) - Ad tracking and attribution platform.
- ![Analytics](image/dot_2.gif) [Rockerbox](https://www.rockerbox.com/) - Marketing measurement and attribution.
- ![Analytics](image/dot_3.gif) [RudderStack](https://www.rudderstack.com/) - Customer data infrastructure.
- ![Analytics](image/dot_4.gif) [Segment](https://segment.com/) - Customer data infrastructure.
- ![Analytics](image/dot_5.gif) [Singular](https://www.singular.net/) - Marketing analytics and attribution.
- ![Analytics](image/dot_1.gif) [Supermetrics](https://supermetrics.com/) - Marketing data integration and reporting.
- ![Analytics](image/dot_2.gif) [Tableau](https://www.tableau.com/) - Business intelligence and data visualization.
- ![Analytics](image/dot_3.gif) [Tealium](https://www.tealium.com/) - Customer data platform and tag management.
- ![Analytics](image/dot_4.gif) [Tenjin](https://www.tenjin.com/) - Mobile marketing analytics and attribution.
- ![Analytics](image/dot_5.gif) [Treasure Data](https://www.treasuredata.com/) - Customer data platform.
- ![Analytics](image/dot_1.gif) [Triple Whale](https://www.triplewhale.com/) - Ecommerce analytics and attribution.
- ![Analytics](image/dot_2.gif) [TUNE](https://www.tune.com/) - Partner marketing and attribution platform.
- ![Analytics](image/dot_3.gif) [Voluum](https://voluum.com/) - Campaign tracking and optimization.
- ![Analytics](image/dot_4.gif) [Whatagraph](https://whatagraph.com/) - Marketing reporting and analytics.
- ![Analytics](image/dot_5.gif) [Windsor.ai](https://www.windsor.ai/) - Marketing data integration and attribution.

## Ad Operations, Workflow & Sales

- ![Operations](image/dot_1.gif) [Adslot](https://www.adslot.com/) - Media trading and workflow technology.
- ![Operations](image/dot_2.gif) [AdTech LeadGen Agent Skills](https://github.com/adops-tool/AdTech-LeadGen-agent-skills) - Agent skills and workflows for ad-tech lead generation.
- ![Operations](image/dot_3.gif) [Advendio](https://www.advendio.com/) - Media sales and order management platform.
- ![Operations](image/dot_4.gif) [Bionic](https://www.bionic-ads.com/) - Media planning and advertising operations software.
- ![Operations](image/dot_5.gif) [Boostr](https://www.boostr.com/) - CRM and order management for media companies.
- ![Operations](image/dot_1.gif) [FatTail](https://www.fattail.com/) - Digital advertising sales and order management.
- ![Operations](image/dot_2.gif) [Google Ad Manager Help](https://support.google.com/admanager/) - Product help and operational guidance.
- ![Operations](image/dot_3.gif) [Google Publisher Partner directory](https://www.google.com/ads/publisher/partners/find-a-partner/) - Find Google-certified publisher partners.
- ![Operations](image/dot_4.gif) [Lineup Systems](https://www.lineup.com/) - Media sales and advertising operations software.
- ![Operations](image/dot_5.gif) [Matrix for Media](https://www.matrixformedia.com/) - Media sales and order management.
- ![Operations](image/dot_1.gif) [Naviga](https://www.navigaglobal.com/) - Media business and publishing technology.
- ![Operations](image/dot_2.gif) [Operative](https://www.operative.com/) - Media operations and advertising management.
- ![Operations](image/dot_3.gif) [Placements.io](https://www.placements.io/) - Ad sales and revenue operations platform.

## Creative, Tags & Campaign Utilities

- ![Creative](image/dot_1.gif) [Bannerflow](https://www.bannerflow.com/) - Creative management and banner production.
- ![Creative](image/dot_2.gif) [Campaign Manager asset validator](https://h5validator.appspot.com/dcm/asset) - Validate Campaign Manager creative assets.
- ![Creative](image/dot_3.gif) [Celtra](https://www.celtra.com/) - Creative automation and rich-media ad production.
- ![Creative](image/dot_4.gif) [Creatopy](https://www.creatopy.com/) - Ad design and creative production platform.
- ![Creative](image/dot_5.gif) [DFP GPT Inspector](https://dfpgpt.appspot.com/) - Inspect Google Publisher Tag requests.
- ![Creative](image/dot_1.gif) [FFmpeg](https://ffmpeg.org/) - Multimedia processing toolkit for video and audio.
- ![Creative](image/dot_2.gif) [Flashtalking](https://www.flashtalking.com/) - Ad serving, creative, and measurement technology.
- ![Creative](image/dot_3.gif) [Google Ads Lighthouse plugin](https://github.com/googleads/publisher-ads-lighthouse-plugin) - Audit publisher ad performance with Lighthouse.
- ![Creative](image/dot_4.gif) [Google Tag Generator](https://taggenerator.google.com/) - Create Google advertising and measurement tags.
- ![Creative](image/dot_5.gif) [Google Web Designer](https://webdesigner.withgoogle.com/) - Create HTML5 ads and other web content.
- ![Creative](image/dot_1.gif) [Google Web Designer cached libraries](https://s0.2mdn.net/ads/studio/cached_libs/index.html) - Google-hosted libraries for ad creatives.
- ![Creative](image/dot_2.gif) [GSAP](https://gsap.com/) - JavaScript animation toolkit used for rich-media creatives.
- ![Creative](image/dot_3.gif) [HandBrake](https://handbrake.fr/) - Open-source video transcoder.
- ![Creative](image/dot_4.gif) [HTML5 Ads Validator](https://h5validator.appspot.com/adwords/asset) - Validate HTML5 Google Ads assets.
- ![Creative](image/dot_5.gif) [Innovid](https://www.innovid.com/) - CTV advertising, delivery, and measurement.
- ![Creative](image/dot_1.gif) [Jivox](https://www.jivox.com/) - Personalized digital advertising and creative automation.
- ![Creative](image/dot_2.gif) [Rich Media Gallery Tools](https://richmediagallery.com/tools/) - Rich-media creative resources and utilities.
- ![Creative](image/dot_3.gif) [SpotX Tag Generator](https://www.spotx.tv/tag-generator/) - Generate video advertising tags.
- ![Creative](image/dot_4.gif) [Squoosh](https://squoosh.app/) - Browser-based image compression and conversion.
- ![Creative](image/dot_5.gif) [TinyPNG](https://tinypng.com/) - Compress PNG and JPEG assets.

## Browser Extensions & AdOps Debugging

- ![Extensions](image/dot_1.gif) [Ad Network Logger](https://chromewebstore.google.com/detail/ad-network-logger/obplbeempbagbggnobgechlhpldmlfll) - Monitor advertising network requests.
- ![Extensions](image/dot_2.gif) [Adswerve Datalayer Inspector](https://chromewebstore.google.com/detail/adswerve-datalayer-inspec/kmcbdogdandhihllalknlcjfpdjcleom) - Inspect data layer events.
- ![Extensions](image/dot_3.gif) [Adtrace GAM Inspector](https://github.com/adops-tool/adtrace-gam-inspector) - Inspect Google Ad Manager setup and page ad calls.
- ![Extensions](image/dot_4.gif) [AdWizard](https://chromewebstore.google.com/detail/adwizard/kndnhcfdajkaickocacghchhpieogbjh) - Browser-based ad operations helper.
- ![Extensions](image/dot_5.gif) [Clear Cache](https://chromewebstore.google.com/detail/clear-cache/cppjkneekbjaeellbfkmgnhonkkjfpdn) - Clear browser cache during implementation testing.
- ![Extensions](image/dot_1.gif) [CMP Validator](https://chromewebstore.google.com/detail/cmp-validator/ffhhjklgcfabkpholngojpkijlafjooc) - Check consent management platform signals.
- ![Extensions](image/dot_2.gif) [Dataslayer](https://chromewebstore.google.com/detail/dataslayer/ikbablmmjldhamhcldjjigniffkkjgpo) - Debug data layers and marketing tags.
- ![Extensions](image/dot_3.gif) [DFP/GPT Inspector](https://chromewebstore.google.com/detail/dfp-gpt-inspector/kfahnbecdeidpfobpbpklnbclgbfjkhm) - Inspect Google Publisher Tag requests and ad slots.
- ![Extensions](image/dot_4.gif) [EditThisCookie](https://chromewebstore.google.com/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) - Inspect and manage browser cookies.
- ![Extensions](image/dot_5.gif) [Ghostery](https://chromewebstore.google.com/detail/ghostery-tracker-ad-block/mlomiejdfkolichcflejclcbmpeaniij) - Inspect and manage trackers and advertising scripts.
- ![Extensions](image/dot_1.gif) [Google Tag Assistant](https://chromewebstore.google.com/detail/tag-assistant-companion/jmekfmbnaedfebfnmakmokmlfpblbfdm) - Debug Google tags and measurement setup.
- ![Extensions](image/dot_2.gif) [Header Bidding Inspector](https://chromewebstore.google.com/detail/header-bidding-inspector/jbkfcjnhdhckflpdjblpcjbegohphdnp) - Inspect header bidding activity in pages.
- ![Extensions](image/dot_3.gif) [HeaderBid Expert extension](https://chromewebstore.google.com/detail/headerbid-expert/cgfkddgbnfplidbfapbbnclbkkbchdhg) - Tools for diagnosing header bidding.
- ![Extensions](image/dot_4.gif) [JSON Viewer](https://chromewebstore.google.com/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh) - Format JSON responses in the browser.
- ![Extensions](image/dot_5.gif) [Lines Checker: ads.txt/app-ads.txt/sellers.json](https://chromewebstore.google.com/detail/lines-checker-adstxtapp-a/gekfhoohhgameebogjaaocnbbdildejb) - Validate ads.txt and app-ads.txt files, find errors and duplicates, and check seller IDs against sellers.json.
- ![Extensions](image/dot_1.gif) [Mass Ads / App Ads Checker](https://chromewebstore.google.com/detail/mass-ads-app-ads-checker/gmojbjflbpipemmhpbhpfhegkmoeobmg) - Check ads.txt and app-ads.txt at scale.
- ![Extensions](image/dot_2.gif) [ModHeader](https://chromewebstore.google.com/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj) - Modify HTTP request headers for testing.
- ![Extensions](image/dot_3.gif) [Omnibug](https://chromewebstore.google.com/detail/omnibug/bknpehncffejahipecakbfkomebjmokl) - Inspect analytics and marketing requests.
- ![Extensions](image/dot_4.gif) [Programmatic ad-scanner](https://chromewebstore.google.com/detail/programmatic-ad-scanner/cbimifbdmnobhmnpclljjnnaggcialof) - Inspect page ad slots and identify common ad-tech signals, including GPT, Prebid.js, and Amazon APS.
- ![Extensions](image/dot_5.gif) [PubGuru Ad Inspector](https://chromewebstore.google.com/detail/pubguru-ad-inspector/nnoilpdinmjmdfpkdkbbecddgmflbdce) - Inspect ads and publisher configuration.
- ![Extensions](image/dot_1.gif) [Requestly](https://chromewebstore.google.com/detail/requestly-intercept-modif/mdnleldcmiljblolnjhpnblkcekpdkpa) - Intercept and modify web requests.
- ![Extensions](image/dot_2.gif) [Sellers.json Inspector](https://chromewebstore.google.com/detail/sellersjson-inspector/neboddkndfhfoeoolmdfgeelajmpdkfm) - Parse and inspect sellers.json and buyers.json files, with seller-ID checks against publisher ads.txt files.
- ![Extensions](image/dot_3.gif) [TCF Auditor](https://chromewebstore.google.com/detail/tcf-auditor/jcniohndgobdkelnbpbaogfhabjjkbkb) - Inspect consent framework behavior.
- ![Extensions](image/dot_4.gif) [User-Agent Switcher](https://chromewebstore.google.com/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg) - Test delivery behavior with alternate user agents.
- ![Extensions](image/dot_5.gif) [Web Vitals extension](https://chromewebstore.google.com/detail/web-vitals/ahfhijdlegdabablpippeagghigmibma) - Measure Core Web Vitals in the browser.

## Developer Tooling & Testing

- ![Developer Tools](image/dot_1.gif) [BrowserStack](https://www.browserstack.com/) - Cross-browser and device testing.
- ![Developer Tools](image/dot_2.gif) [bsm/openrtb](https://github.com/bsm/openrtb) - OpenRTB implementation for Go.
- ![Developer Tools](image/dot_3.gif) [Charles Proxy](https://www.charlesproxy.com/) - HTTP proxy for inspecting web and app traffic.
- ![Developer Tools](image/dot_4.gif) [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Browser debugging and performance tools.
- ![Developer Tools](image/dot_5.gif) [CodePen](https://codepen.io/) - Online editor for front-end prototypes.
- ![Developer Tools](image/dot_1.gif) [CodeSandbox](https://codesandbox.io/) - Cloud development environment.
- ![Developer Tools](image/dot_2.gif) [DebugBear](https://www.debugbear.com/) - Website performance monitoring and diagnostics.
- ![Developer Tools](image/dot_3.gif) [Fiddler](https://www.telerik.com/fiddler) - Web debugging proxy.
- ![Developer Tools](image/dot_4.gif) [FIZZ OpenRTB Inspector](https://fizzkit.net/tools/openrtb-inspector/) - Inspect OpenRTB bid requests and responses.
- ![Developer Tools](image/dot_5.gif) [Google Ads .NET](https://github.com/googleads/googleads-dotnet-lib) - .NET client library for Google Ads API.
- ![Developer Tools](image/dot_1.gif) [Google Ads Java](https://github.com/googleads/google-ads-java) - Java client library for Google Ads API.
- ![Developer Tools](image/dot_2.gif) [Google Ads MCP](https://github.com/googleads/google-ads-mcp) - Model Context Protocol server for Google Ads.
- ![Developer Tools](image/dot_3.gif) [Google Ads Node](https://github.com/googleads/google-ads-node) - Node.js client library for Google Ads API.
- ![Developer Tools](image/dot_4.gif) [Google Ads PHP](https://github.com/googleads/googleads-php-lib) - PHP client library for Google Ads API.
- ![Developer Tools](image/dot_5.gif) [Google Ads Python](https://github.com/googleads/google-ads-python) - Python client library for Google Ads API.
- ![Developer Tools](image/dot_1.gif) [Google Ads Ruby](https://github.com/googleads/google-ads-ruby) - Ruby client library for Google Ads API.
- ![Developer Tools](image/dot_2.gif) [Google Consent SDK Android](https://github.com/googleads/googleads-consent-sdk-android) - Consent SDK for Android.
- ![Developer Tools](image/dot_3.gif) [Google Consent SDK iOS](https://github.com/googleads/googleads-consent-sdk-ios) - Consent SDK for iOS.
- ![Developer Tools](image/dot_4.gif) [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/) - Audit performance, accessibility, and web quality.
- ![Developer Tools](image/dot_5.gif) [Google Mobile Ads Android examples](https://github.com/googleads/googleads-mobile-android-examples) - Android SDK samples.
- ![Developer Tools](image/dot_1.gif) [Google Mobile Ads iOS examples](https://github.com/googleads/googleads-mobile-ios-examples) - iOS SDK samples.
- ![Developer Tools](image/dot_2.gif) [GTmetrix](https://gtmetrix.com/) - Website performance and speed analysis.
- ![Developer Tools](image/dot_3.gif) [Hoppscotch](https://hoppscotch.io/) - Open-source API development environment.
- ![Developer Tools](image/dot_4.gif) [HTTP Toolkit](https://httptoolkit.com/) - Intercept and inspect HTTP traffic.
- ![Developer Tools](image/dot_5.gif) [Insomnia](https://insomnia.rest/) - API client and testing tool.
- ![Developer Tools](image/dot_1.gif) [jq play](https://jqplay.org/) - Experiment with jq filters.
- ![Developer Tools](image/dot_2.gif) [JSFiddle](https://jsfiddle.net/) - Share and test HTML, CSS, and JavaScript.
- ![Developer Tools](image/dot_3.gif) [JSONLint](https://jsonlint.com/) - Validate JSON documents.
- ![Developer Tools](image/dot_4.gif) [JWT.io](https://jwt.io/) - Decode and inspect JSON Web Tokens.
- ![Developer Tools](image/dot_5.gif) [LambdaTest](https://www.lambdatest.com/) - Cross-browser testing platform.
- ![Developer Tools](image/dot_1.gif) [mitmproxy](https://mitmproxy.org/) - Open-source interactive HTTPS proxy.
- ![Developer Tools](image/dot_2.gif) [mxmCherry/openrtb](https://github.com/mxmCherry/openrtb) - OpenRTB Go library.
- ![Developer Tools](image/dot_3.gif) [ngrok](https://ngrok.com/) - Secure tunnels to local development services.
- ![Developer Tools](image/dot_4.gif) [Open Measurement Android](https://github.com/googleads/open-measurement-android) - Open Measurement SDK for Android.
- ![Developer Tools](image/dot_5.gif) [Open Measurement iOS](https://github.com/googleads/open-measurement-ios) - Open Measurement SDK for iOS.
- ![Developer Tools](image/dot_1.gif) [OpenRTB Go](https://github.com/metabrainz/openrtb-go) - Go implementation of OpenRTB structures.
- ![Developer Tools](image/dot_2.gif) [PageSpeed Insights](https://pagespeed.web.dev/) - Analyze page performance and Core Web Vitals.
- ![Developer Tools](image/dot_3.gif) [Postman](https://www.postman.com/) - API development and testing workspace.
- ![Developer Tools](image/dot_4.gif) [Proxyman](https://proxyman.io/) - HTTP debugging proxy for developers.
- ![Developer Tools](image/dot_5.gif) [Regex101](https://regex101.com/) - Build and test regular expressions.
- ![Developer Tools](image/dot_1.gif) [ReqBin](https://reqbin.com/) - Online HTTP request testing.
- ![Developer Tools](image/dot_2.gif) [Sauce Labs](https://saucelabs.com/) - Cloud testing for web and mobile applications.
- ![Developer Tools](image/dot_3.gif) [SpeedCurve](https://speedcurve.com/) - Web performance monitoring.
- ![Developer Tools](image/dot_4.gif) [URL Decoder](https://www.urldecoder.org/) - Decode and encode URL components.
- ![Developer Tools](image/dot_5.gif) [Vungle OpenRTB](https://github.com/Vungle/openrtb) - OpenRTB-related project from Vungle.
- ![Developer Tools](image/dot_1.gif) [Webhook.site](https://webhook.site/) - Inspect incoming HTTP requests and webhooks.
- ![Developer Tools](image/dot_2.gif) [WebPageTest](https://www.webpagetest.org/) - Website performance testing.
- ![Developer Tools](image/dot_3.gif) [Wireshark](https://www.wireshark.org/) - Network protocol analyzer.

## Open-Source Ad Servers, RTB & Publisher Engineering

- ![Open Source](image/dot_1.gif) [Ad Ops repositories by adops-tool](https://github.com/adops-tool) - Open-source utilities and projects for ad operations.
- ![Open Source](image/dot_2.gif) [Ad Server Platform list](https://github.com/ishandutta2007/Awesome-Ad-Serving-Platform) - Community-maintained directory of ad serving platforms.
- ![Open Source](image/dot_3.gif) [Ad server: Wikia Ad Engine](https://github.com/Wikia/ad-engine) - Publisher advertising codebase from Fandom/Wikia.
- ![Open Source](image/dot_4.gif) [Automattic ad-tracker](https://github.com/Automattic/ad-tracker) - Advertising tracking utility from Automattic.
- ![Open Source](image/dot_5.gif) [Awesome AdTech](https://github.com/ClearcodeHQ/awesome-adtech) - Curated links to ad-tech concepts, products, and projects.
- ![Open Source](image/dot_1.gif) [Guardian commercial core](https://github.com/guardian/commercial-core) - The Guardian's commercial frontend components.
- ![Open Source](image/dot_2.gif) [NYTimes DFP Ads](https://github.com/nytimes/dfp-ads) - Google ad tag integration utilities from The New York Times.
- ![Open Source](image/dot_3.gif) [OpenRTB for Unity](https://github.com/unity3d-kr/openrtb) - OpenRTB-related Unity project.
- ![Open Source](image/dot_4.gif) [RTBKit](https://github.com/rtbkit/rtbkit) - Open-source real-time bidding framework for building and deploying bidders.
- ![Open Source](image/dot_5.gif) [Spring Media advertising config](https://github.com/spring-media/advertising-config) - Advertising configuration project from Spring Media.
- ![Open Source](image/dot_1.gif) [SSPServer](https://github.com/sspserver/sspserver) - Open-source supply-side platform project.
- ![Open Source](image/dot_2.gif) [Vanilla RTB](https://github.com/vanilla-rtb/vrtb) - Open-source real-time bidding project.
- ![Open Source](image/dot_3.gif) [Vox Concert Ad Manager](https://github.com/voxmedia/concert-ad-manager) - Ad management application from Vox Media.
- ![Open Source](image/dot_4.gif) [XRTB](https://github.com/xrtb/XRTB) - Open-source real-time bidding project.

## Mobile Advertising, App Monetization & Gaming

- ![Mobile](image/dot_1.gif) [AdColony](https://www.adcolony.com/) - In-app video advertising technology.
- ![Mobile](image/dot_2.gif) [AdInPlay](https://www.adinplay.com/) - Advertising monetization for browser games.
- ![Mobile](image/dot_3.gif) [Adjoe](https://www.adjoe.io/) - Mobile advertising and rewarded engagement platform.
- ![Mobile](image/dot_4.gif) [AppLovin](https://www.applovin.com/) - Mobile marketing and monetization platform.
- ![Mobile](image/dot_5.gif) [AppLovin MAX](https://www.applovin.com/max/) - Mobile mediation and monetization platform.
- ![Mobile](image/dot_1.gif) [Chartboost](https://www.chartboost.com/) - Mobile game advertising and monetization.
- ![Mobile](image/dot_2.gif) [CrazyGames](https://www.crazygames.com/) - Browser game platform and publisher ecosystem.
- ![Mobile](image/dot_3.gif) [Digital Turbine](https://www.digitalturbine.com/) - Mobile growth and advertising platform.
- ![Mobile](image/dot_4.gif) [Enthusiast Gaming](https://www.enthusiastgaming.com/) - Gaming media, communities, and monetization.
- ![Mobile](image/dot_5.gif) [Fyber](https://www.fyber.com/) - Mobile monetization and mediation technology.
- ![Mobile](image/dot_1.gif) [GameDistribution](https://gamedistribution.com/) - HTML5 game distribution and monetization network.
- ![Mobile](image/dot_2.gif) [GameMonetize](https://www.gamemonetize.com/) - HTML5 game distribution and monetization.
- ![Mobile](image/dot_3.gif) [Google AdMob](https://admob.google.com/) - Mobile app monetization platform.
- ![Mobile](image/dot_4.gif) [Google Mobile Ads SDK](https://developers.google.com/admob) - Google mobile advertising SDK documentation.
- ![Mobile](image/dot_5.gif) [InMobi](https://www.inmobi.com/) - Mobile advertising and marketing platform.
- ![Mobile](image/dot_1.gif) [ironSource](https://www.is.com/) - Mobile app monetization and user acquisition technology.
- ![Mobile](image/dot_2.gif) [Kongregate](https://www.kongregate.com/) - Online games platform and developer community.
- ![Mobile](image/dot_3.gif) [Liftoff](https://liftoff.io/) - Mobile app marketing and monetization.
- ![Mobile](image/dot_4.gif) [Mintegral](https://www.mintegral.com/) - Mobile programmatic advertising platform.
- ![Mobile](image/dot_5.gif) [Moloco](https://www.moloco.com/) - Machine-learning advertising and app growth platform.
- ![Mobile](image/dot_1.gif) [Network N](https://www.network-n.com/) - Gaming media and advertising network.
- ![Mobile](image/dot_2.gif) [Ogury](https://www.ogury.com/) - Mobile advertising and audience solutions.
- ![Mobile](image/dot_3.gif) [Overwolf](https://www.overwolf.com/) - In-game apps and advertising platform.
- ![Mobile](image/dot_4.gif) [Pangle](https://www.pangleglobal.com/) - Global advertising platform for apps.
- ![Mobile](image/dot_5.gif) [Poki](https://poki.com/) - Online games platform and developer publishing program.
- ![Mobile](image/dot_1.gif) [Smaato](https://www.smaato.com/) - Global omnichannel ad exchange.
- ![Mobile](image/dot_2.gif) [Tapjoy](https://www.tapjoy.com/) - In-app advertising and user acquisition.
- ![Mobile](image/dot_3.gif) [Unity Ads](https://unity.com/products/unity-ads) - Advertising and monetization for games and apps.
- ![Mobile](image/dot_4.gif) [Vungle](https://www.vungle.com/) - Mobile performance marketing and monetization.
- ![Mobile](image/dot_5.gif) [Y8 Games](https://www.y8.com/) - Browser games platform and publisher network.

## Ad-Tech Research & Site Discovery

- ![Research](image/dot_1.gif) [42matters](https://42matters.com/) - App market data and intelligence APIs.
- ![Research](image/dot_2.gif) [Adbeat](https://www.adbeat.com/) - Display advertising intelligence and competitor research.
- ![Research](image/dot_3.gif) [AdClarity](https://adclarity.com/) - Digital advertising intelligence and competitive insights.
- ![Research](image/dot_4.gif) [AppBrain](https://www.appbrain.com/) - Android app market data and advertising insights.
- ![Research](image/dot_5.gif) [Appfigures](https://appfigures.com/) - App analytics, rankings, and market intelligence.
- ![Research](image/dot_1.gif) [Apptopia](https://www.apptopia.com/) - Mobile app market and competitive intelligence.
- ![Research](image/dot_2.gif) [BuiltWith](https://builtwith.com/) - Technology profiling and web intelligence.
- ![Research](image/dot_3.gif) [data.ai](https://www.data.ai/) - Mobile app market intelligence.
- ![Research](image/dot_4.gif) [Jounce Media](https://www.jouncemedia.com/) - Programmatic supply-chain research and analysis.
- ![Research](image/dot_5.gif) [MediaRadar](https://www.mediaradar.com/) - Advertising sales and competitive intelligence.
- ![Research](image/dot_1.gif) [MixRank](https://mixrank.com/) - App, company, and advertising intelligence.
- ![Research](image/dot_2.gif) [MobileAction](https://www.mobileaction.co/) - App intelligence and mobile growth analytics.
- ![Research](image/dot_3.gif) [MXToolbox](https://mxtoolbox.com/) - DNS, email, and domain diagnostics.
- ![Research](image/dot_4.gif) [NerdyData](https://nerdydata.com/) - Search websites by source code and technology.
- ![Research](image/dot_5.gif) [Pathmatics](https://www.pathmatics.com/) - Digital advertising competitive intelligence.
- ![Research](image/dot_1.gif) [PublicWWW](https://publicwww.com/) - Search source code and discover web technologies.
- ![Research](image/dot_2.gif) [SecurityTrails](https://securitytrails.com/) - DNS and domain intelligence.
- ![Research](image/dot_3.gif) [Semrush](https://www.semrush.com/) - Digital marketing, search, and competitive research tools.
- ![Research](image/dot_4.gif) [Sensor Tower](https://sensortower.com/) - App intelligence, advertising, and market insights.
- ![Research](image/dot_5.gif) [Similarweb](https://www.similarweb.com/) - Website and app traffic intelligence.
- ![Research](image/dot_1.gif) [Sincera](https://www.sincera.io/) - Ad-tech data and supply-chain intelligence.
- ![Research](image/dot_2.gif) [Sincera Open](https://open.sincera.io/) - Open advertising ecosystem data.
- ![Research](image/dot_3.gif) [SpyFu](https://www.spyfu.com/) - Search advertising and SEO competitive research.
- ![Research](image/dot_4.gif) [URLScan.io](https://urlscan.io/) - Analyze and inspect websites and their requests.
- ![Research](image/dot_5.gif) [ViewDNS](https://viewdns.info/) - DNS, IP, and domain lookup utilities.
- ![Research](image/dot_1.gif) [Wappalyzer](https://www.wappalyzer.com/) - Identify website technologies.
- ![Research](image/dot_2.gif) [WhatRunsWhere](https://www.whatrunswhere.com/) - Competitive display advertising intelligence.

## Privacy Sandbox: Retired APIs & Current Status

- ![Privacy Sandbox](image/dot_1.gif) [Attribution (W3C)](https://github.com/w3c/attribution) - W3C effort to develop an interoperable, privacy-preserving web attribution standard.
- ![Privacy Sandbox](image/dot_2.gif) [Attribution Reporting API (retired)](https://github.com/WICG/attribution-reporting-api) - Archived proposal for privacy-preserving ad measurement; Google retired this API in 2025.
- ![Privacy Sandbox](image/dot_3.gif) [FLEDGE documentation archive](https://github.com/privacysandbox/fledge-docs) - Archived design documentation for FLEDGE, an earlier iteration of the now-retired Protected Audience API.
- ![Privacy Sandbox](image/dot_4.gif) [Privacy Sandbox feature status](https://privacysandbox.google.com/overview/status) - Google’s current status page for Privacy Sandbox APIs and platform features.
- ![Privacy Sandbox](image/dot_5.gif) [Privacy Sandbox retirement announcement](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies) - Google’s October 2025 notice lists the APIs it retired and the areas where work continues.
- ![Privacy Sandbox](image/dot_1.gif) [Protected Audience documentation (retired)](https://github.com/privacysandbox/protected-auction-services-docs) - Archived documentation for Protected Audience server-side services; the API was retired in 2025.
- ![Privacy Sandbox](image/dot_2.gif) [Topics API explainer (retired)](https://github.com/patcg-individual-drafts/topics) - Archived proposal and explainer for the Topics API, retired by Google in 2025.
- ![Privacy Sandbox](image/dot_3.gif) [TURTLEDOVE proposal](https://github.com/WICG/turtledove) - Archived early proposal that informed later privacy-preserving remarketing work.

## Learning, News & Communities

- ![Learning](image/dot_1.gif) [Ad Age](https://adage.com/) - Advertising and marketing news.
- ![Learning](image/dot_2.gif) [AdExchanger](https://www.adexchanger.com/) - News and analysis covering ad tech and data.
- ![Learning](image/dot_3.gif) [AdMonsters](https://www.admonsters.com/) - Publisher and ad operations community and events.
- ![Learning](image/dot_4.gif) [AdOps Doctor](https://adopsdoctor.com/) - Ad operations services and resources.
- ![Learning](image/dot_5.gif) [AdOps Insider](https://www.adopsinsider.com/) - Practical advertising operations articles.
- ![Learning](image/dot_1.gif) [AdProfs](https://adprofs.co/) - Community and resources for advertising professionals.
- ![Learning](image/dot_2.gif) [AdTech God](https://www.adtechgod.com/) - Ad-tech education and industry resources.
- ![Learning](image/dot_3.gif) [AdWeek](https://www.adweek.com/) - Advertising, marketing, and media industry news.
- ![Learning](image/dot_4.gif) [Analytics Mania](https://www.analyticsmania.com/) - Google Analytics and Tag Manager guides.
- ![Learning](image/dot_5.gif) [Beeler.Tech](https://www.beeler.tech/) - Programmatic advertising insights and community.
- ![Learning](image/dot_1.gif) [Clearcode AdTech Book](https://clearcode.cc/adtech-book/) - Introductory guide to ad-tech concepts.
- ![Learning](image/dot_2.gif) [Digiday](https://digiday.com/) - Digital media, marketing, and publishing news.
- ![Learning](image/dot_3.gif) [ExchangeWire](https://www.exchangewire.com/) - Programmatic and digital media news.
- ![Learning](image/dot_4.gif) [Google Skillshop](https://skillshop.withgoogle.com/) - Google Ads and analytics training.
- ![Learning](image/dot_5.gif) [Marketingecture](https://www.marketecture.tv/) - Marketing technology interviews and education.
- ![Learning](image/dot_1.gif) [MediaPost](https://www.mediapost.com/) - Advertising and media news and analysis.
- ![Learning](image/dot_2.gif) [Mobile Dev Memo](https://mobiledevmemo.com/) - Mobile growth and advertising analysis.
- ![Learning](image/dot_3.gif) [Programmatic Ads](https://github.com/programmatic-ads-io) - Programmatic advertising projects and resources.
- ![Learning](image/dot_4.gif) [Publisher University](https://publisheruniversity.withgoogle.com/) - Publisher-focused learning resources.
- ![Learning](image/dot_5.gif) [r/adops](https://www.reddit.com/r/adops/) - Community for advertising operations professionals.
- ![Learning](image/dot_1.gif) [r/adtech](https://www.reddit.com/r/adtech/) - Community about advertising technology.
- ![Learning](image/dot_2.gif) [r/programmatic](https://www.reddit.com/r/programmatic/) - Discussion of programmatic advertising.
- ![Learning](image/dot_3.gif) [Simo Ahava](https://www.simoahava.com/) - Analytics, tagging, and measurement tutorials.
- ![Learning](image/dot_4.gif) [The Drum](https://www.thedrum.com/) - Global marketing and media coverage.
- ![Learning](image/dot_5.gif) [The Trade Desk Edge Academy](https://www.thetradedesk.com/us/edge-academy) - Digital media and programmatic learning.
- ![Learning](image/dot_1.gif) [VideoWeek](https://www.videoweek.com/) - Video advertising and streaming industry news.

## Contributing

Found a useful resource or spotted an outdated link? Please read [CONTRIBUTING.md](CONTRIBUTING.md) and open a pull request.

## License

This list is available under the repository's [CC0 1.0 Universal](LICENSE). Product names and trademarks belong to their respective owners.
