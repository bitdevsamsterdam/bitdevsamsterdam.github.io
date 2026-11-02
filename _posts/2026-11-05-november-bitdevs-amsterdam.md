---
layout: post
type: socratic
title: "BitDevs @ Bitcoin Amsterdam, November 5, 2026"
published: true
---

## BitDevs Amsterdam meeting 032!

This time BitDevs takes place at the **Bitcoin Amsterdam** conference at the **SugarFactory**. Please note that **no conference ticket is required** to attend.

### Thursday, November 5th, 2026 @ 5:30PM

The meetup runs from 5:30PM to 7:30PM at the SugarFactory, in the room off the main community walkway, where stage 3 will be.

As a reminder, the ground rules of BitDevs are as follows:

1. No photos, videos, or recordings.
1. [Chatham House Rule](https://en.wikipedia.org/wiki/Chatham_House_Rule): you may
   reiterate the contents of the meeting *without* attribution.

These rules exist so that BitDevs participants can speak freely within the event.

### Agenda

#### Security incidents

- **Binance $6B hack**: On October 29, attackers drained roughly $6.3 billion from Binance across multiple chains in about 20 minutes, the largest crypto theft on record, which the FBI has attributed to North Korea.
  - [https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history](https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history)
  - [https://www.nbcnews.com/business/business-news/fbi-says-north-korea-was-6-billion-binance-crypto-hack-rcna606758](https://www.nbcnews.com/business/business-news/fbi-says-north-korea-was-6-billion-binance-crypto-hack-rcna606758)
  - [https://www.coindesk.com/business/2026/10/29/potential-multi-billion-binance-hack-hitting-crypto-markets](https://www.coindesk.com/business/2026/10/29/potential-multi-billion-binance-hack-hitting-crypto-markets)

- **BTCPay Server hot wallets swept**: BTCPay Server is receiving reports of unauthorized attackers sweeping hot wallets on BTCPay instances and has urged operators to shut their servers down until the investigation is complete.
  - [https://x.com/BtcpayServer/status/2117020340815819262](https://x.com/BtcpayServer/status/2117020340815819262)

- **lnd mitigation for a Linux kernel use-after-free**: lnd v0.20.7 and v0.21.6 turn off Go's MPTCP support to mitigate CVE-2026-98432, a use-after-free in the Linux kernel's IPv4 TCP stack, though only a kernel patch fully protects network-facing services.
  - [https://x.com/roasbeef/status/2116301109174407547](https://x.com/roasbeef/status/2116301109174407547)

- **CLN self-referential channel announcement DoS**: A `channel_announcement` naming the same node on both sides crashes Core Lightning, and because it is persisted to disk the node keeps crashing on every restart; it affects v25.02 through v26.04 and is fixed in v26.04.1.
  - [https://delvingbitcoin.org/t/cln-self-referential-channel-announcement-dos-disclosure/2974](https://delvingbitcoin.org/t/cln-self-referential-channel-announcement-dos-disclosure/2974)

- **Second's Ark server exploited**: A bug in the boarding flow let an attacker register boards without the server's cosignature, exit them to his own wallet, and also spend the same VTXOs over Lightning, taking 0.75 BTC of Second's own liquidity. User funds were never at risk because VTXOs sit on pre-signed exit paths the server can't spend.
  - [https://stacker.news/items/1591231](https://stacker.news/items/1591231)

#### Bitcoin Core

- **Bitcoin Core security policy update**: As LLMs make bugs easier to rediscover, Bitcoin Core will shorten the embargo for vulnerabilities considered easy to find, backporting and releasing fixes as soon as possible with a security advisory.
  - [https://gnusha.org/pi/bitcoindev/1ehBdwhbU-1cUjU5SjRxn75XNUBvIfNbkfqPCJRFPlOfsBu5gHWotmNRNxcMirTl1baT2H-zBfJMeWM6rl-XJG8zV6gHf8vQ9b_TRB9vnIk=@antoinep.com/](https://gnusha.org/pi/bitcoindev/1ehBdwhbU-1cUjU5SjRxn75XNUBvIfNbkfqPCJRFPlOfsBu5gHWotmNRNxcMirTl1baT2H-zBfJMeWM6rl-XJG8zV6gHf8vQ9b_TRB9vnIk=@antoinep.com/)

#### Privacy

- **Shielded Bitcoin**: A Zcash-style shielded-note protocol for private transfers on Bitcoin L1 without consensus changes, where all data is published on Bitcoin and validity is enforced with zero-knowledge proofs.
  - [https://www.allocinit.xyz/uploads/shielded-bitcoin.pdf](https://www.allocinit.xyz/uploads/shielded-bitcoin.pdf)

- **Silent payments for multiparty wallets**: Proposes a way for FROST and MuSig2 wallets to send silent payments by combining per-signer ECDH contributions, each backed by a DLEQ proof, into a single BIP-374-compatible proof.
  - [https://delvingbitcoin.org/t/silent-payments-for-multiparty-wallets/2960](https://delvingbitcoin.org/t/silent-payments-for-multiparty-wallets/2960)

#### Lightning and layer 2

- **Wavelength live on mainnet**: Lightning Labs' Wavelength SDK is now live on mainnet, letting humans and agents send and receive bitcoin with a few self-custodial API calls and no node or liquidity to manage.
  - [https://x.com/lightning/status/2113637153070542859](https://x.com/lightning/status/2113637153070542859)

- **LayerTree**: A covenant-based scaling design from Lightning Labs where one UTXO holds the balances of millions of users in an off-chain Merkle-sum tree, and any user can exit in a single transaction without pre-signing.
  - [https://x.com/roasbeef/status/2110813488822239619](https://x.com/roasbeef/status/2110813488822239619)

#### Community

- Want to submit a discussion topic? Open an issue or PR at [https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io](https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io)
