---
layout: post
type: socratic
title: "BitDevs Amsterdam, March 5th, 2026"
meetup: https://www.meetup.com/bitdevs-amsterdam/events/TODO
published: true
---

## BitDevs Amsterdam meeting 026!

It's time for another BitDevs! A big thanks to [Bitonic](https://www.bitonic.nl) for sponsoring us with the meeting space. Drinks will be provided, so please ensure you have some dinner beforehand or bring it along to the seminar.

### Thursday, March 5th, 2026 @ 7PM

Doors open at 6:30PM and we will try to start promptly at 7PM. As a reminder, the ground rules of BitDevs are as follows:

1. No photos, videos, or recordings.
1. [Chatham House Rule](https://en.wikipedia.org/wiki/Chatham_House_Rule): you may
   reiterate the contents of the meeting *without* attribution.

These rules exist so that BitDevs participants can speak freely within the event.

### Agenda

- **hArk (hash-lock-Ark)**: A major Ark protocol evolution that eliminates synchronous interactivity during rounds. Instead of requiring all participants to be online simultaneously to sign transactions, the server generates unique secrets for each VTXO, allowing participants to claim their funds asynchronously.
  - [https://x.com/2ndbtc/status/2015401100355002626](https://x.com/2ndbtc/status/2015401100355002626)

- **ZK Statechains**: Replaces traditional statechain ledgers with zero-knowledge proofs to validate ownership transfers of Bitcoin UTXOs while maintaining privacy, combining statechain exit mechanics with a "ZK Ledger" that proves key changes and timelock decrements.
  - [https://delvingbitcoin.org/t/zk-statechains-without-states/2166](https://delvingbitcoin.org/t/zk-statechains-without-states/2166)

- **Taproot Quantum Spend Paths**: Proposes a quantum-safe version of Taproot that allows Bitcoin addresses to have multiple spending paths (both quantum-resistant and quantum-vulnerable), letting users continue benefiting from smaller, efficient signatures until quantum computers become a genuine threat.
  - [https://www.bitmex.com/blog/Taproot-Quantum-Spend-Paths](https://www.bitmex.com/blog/Taproot-Quantum-Spend-Paths)

- **Lightning Network surpassed $1B in monthly volume**
  - [https://x.com/SDWouters/status/2024507942708351443](https://x.com/SDWouters/status/2024507942708351443)
  - [River: Bitcoin Adoption 2026](https://river.com/content/bitcoin-adoption-2026) — Bitcoin adoption is accelerating across institutional, business, and individual segments, with the Lightning Network reaching $1 billion in monthly volume and 194 public companies now holding bitcoin on their balance sheets.

- **L402 Apps**: A directory and marketplace for Lightning Network-powered applications and APIs that enable micropayments in Bitcoin. Discover apps that accept L402 payments and call verified Lightning-paywalled API endpoints priced in satoshis.
  - [https://www.l402apps.com/](https://www.l402apps.com/)

- **BIP352 update**: Proposes adding a limit specifying that the number of taproot outputs in a transaction must fit within an unsigned 32-bit integer for silent payments scanning, improving clarity for implementations choosing compatible data types.
  - [https://github.com/bitcoin/bips/pull/2055](https://github.com/bitcoin/bips/pull/2055)

- **sedited added to trusted-keys**: Adds sedited to Bitcoin Core's trusted-keys file, granting cryptographic signing authority for the release process.
  - [https://github.com/bitcoin/bitcoin/pull/34236](https://github.com/bitcoin/bitcoin/pull/34236)

- **Incremental mutation testing in Bitcoin Core**: Applies mutation testing selectively and progressively by focusing only on code changes since the last analysis, dramatically reducing execution time while maintaining the ability to assess whether tests effectively detect introduced bugs.
  - [https://delvingbitcoin.org/t/incremental-mutation-testing-in-the-bitcoin-core/2197](https://delvingbitcoin.org/t/incremental-mutation-testing-in-the-bitcoin-core/2197)

- **Binohash: Transaction Introspection Without Softforks**: A collision-resistant hash function for Bitcoin Script that enables limited transaction introspection without consensus changes.
  - [https://robinlinus.com/binohash.pdf][https://robinlinus.com/binohash.pdf]