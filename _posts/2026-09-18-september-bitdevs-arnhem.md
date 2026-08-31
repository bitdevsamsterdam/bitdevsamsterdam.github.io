---
layout: post
type: socratic
title: "BitDevs Arnhem, September 18, 2026"
published: true
---

## BitDevs Arnhem meeting 031!

It's time for another BitDevs! A big thanks to Four Digits for hosting us at their office. Drinks will be provided, so please ensure you have some dinner beforehand or bring it along to the seminar.

### Friday, September 18th, 2026

The venue is at Jansbinnensingel 26, Arnhem — about a 10 minute walk from Arnhem Centraal train station.

- **Doors open:** 6:30PM
- **Start (sharp):** 7:00PM
- **End (sharp):** 9:00PM

Afterwards we'll head to a nearby café that accepts bitcoin.

As a reminder, the ground rules of BitDevs are as follows:

1. No photos, videos, or recordings.
1. [Chatham House Rule](https://en.wikipedia.org/wiki/Chatham_House_Rule): you may
   reiterate the contents of the meeting *without* attribution.

These rules exist so that BitDevs participants can speak freely within the event.

### Agenda

#### Consensus

- **BIP-110 now closed**: The "Reduced Data Temporary Softfork", which proposed temporarily limiting transaction data fields at the consensus level, has been marked closed following a chain split with stalled mining.
  - [https://github.com/bitcoin/bips/blob/master/bip-0110.mediawiki](https://github.com/bitcoin/bips/blob/master/bip-0110.mediawiki)

#### Security

- **Coldcard entropy hack**: A firmware bug in Coldcard Mk2/Mk3 used a predictable PRNG instead of the secure hardware RNG when generating keys, dropping entropy to ~40 bits and letting attackers brute-force and drain thousands of wallets.
  - [https://www.halborn.com/blog/post/explained-the-coldcard-hack-july-2026](https://www.halborn.com/blog/post/explained-the-coldcard-hack-july-2026)

- **Bitcoin red team**: Calle (callebtc) calls for a coordinated Bitcoin "red team" to proactively hunt and responsibly disclose vulnerabilities across Bitcoin software.
  - [https://x.com/callebtc/status/2085024458012586286](https://x.com/callebtc/status/2085024458012586286)

#### Lightning Network

- **Wavelength**: Lightning Labs' new toolkit that abstracts Lightning behind a simple non-custodial API, letting any developer or AI agent give an app a self-custodial bitcoin wallet without running infrastructure.
  - [https://wavelength.lightning.engineering/](https://wavelength.lightning.engineering/)
  - [https://lightning.engineering/posts/2026-07-21-wavelength-launch/](https://lightning.engineering/posts/2026-07-21-wavelength-launch/)
  - [https://bitcoinmagazine.com/technical/lightning-labs-launches-wavelength-bitcoin-on-easy-mode-for-developers-and-autonomous-agents](https://bitcoinmagazine.com/technical/lightning-labs-launches-wavelength-bitcoin-on-easy-mode-for-developers-and-autonomous-agents)

- **CLN faces a major security vulnerability**: A serious Core Lightning vulnerability has been flagged, with users urged to update; the root issue has not yet been disclosed.
  - [https://x.com/murchandamus/status/2092668704790315288](https://x.com/murchandamus/status/2092668704790315288)
  - **CLN ping-flood DoS disclosure**: A separate, already-disclosed DoS where attackers crash Core Lightning nodes by flooding them with max-size `ping` messages while refusing to read replies, growing the outgoing queue unbounded until an OOM kill; now fixed by routing all messages through proper flow-control gates.
    - [https://delvingbitcoin.org/t/disclosure-crashing-cln-with-a-flood-of-pings/2846](https://delvingbitcoin.org/t/disclosure-crashing-cln-with-a-flood-of-pings/2846)

- **Boltz taken over after security incidents**: Boltz suspended its Bitcoin/Lightning swap service on August 3 after escalating AI-assisted attacks, and its founders have now exited as an unnamed group of Bitcoin veterans takes over to fund and fix it.
  - [https://thedefiant.io/news/infrastructure/boltz-founders-exit-as-unnamed-bitcoin-group-agrees-to-take-over-suspended-swap-service](https://thedefiant.io/news/infrastructure/boltz-founders-exit-as-unnamed-bitcoin-group-agrees-to-take-over-suspended-swap-service)

#### Community

- Want to submit a discussion topic? Open an issue or PR at [https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io](https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io)
