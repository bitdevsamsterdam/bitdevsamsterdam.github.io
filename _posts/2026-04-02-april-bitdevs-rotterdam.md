---
layout: post
type: socratic
title: "BitDevs Rotterdam, April 2, 2026"
meetup: https://www.meetup.com/bitdevs-amsterdam/events/313791500
published: true
---

## BitDevs Rotterdam meeting 027!

It's time for another BitDevs! A big thanks to [Blockrise](https://www.blockrise.com/nl) for sponsoring us with the meeting space. Drinks will be provided, so please ensure you have some dinner beforehand or bring it along to the seminar.

### Thursday, April 2nd, 2026 @ 7PM

Doors open at 6:30PM and we will try to start promptly at 7PM. As a reminder, the ground rules of BitDevs are as follows:

1. No photos, videos, or recordings.
1. [Chatham House Rule](https://en.wikipedia.org/wiki/Chatham_House_Rule): you may
   reiterate the contents of the meeting *without* attribution.

These rules exist so that BitDevs participants can speak freely within the event.

### Agenda

- **Disposing of dust attack UTXOs**: A proposed method for wallet users to dispose of "dust attack" UTXOs, small amounts sent by adversaries to reveal wallet ownership patterns, by creating transactions that use the entire amount for fees with an OP_RETURN output.
  - [https://delvingbitcoin.org/t/disposing-of-dust-attack-utxos/2215](https://delvingbitcoin.org/t/disposing-of-dust-attack-utxos/2215)

- **BIP 54 (Consensus Cleanup) active on Bitcoin Inquisition**: BIP 54 is now active on Bitcoin Inquisition, a specialized Bitcoin Core fork used for testing proposed protocol changes. It includes fixes for known consensus bugs such as Timewarp/Murch-Zawy timestamp attacks, long block validation times from excessive legacy signature operations, the 64-byte transaction Merkle tree weakness, and coinbase transaction duplication.
  - [https://groups.google.com/g/bitcoindev/c/wOVjJoLDWfA](https://groups.google.com/g/bitcoindev/c/wOVjJoLDWfA)

- **Hourglass V2 update**: An update on the Hourglass protocol (V2), a proposed soft fork designed to mitigate the economic damage from potential quantum attacks on lost Bitcoin. It would restrict how quickly vulnerable P2PK funds can be spent to prevent a mass market liquidation event if a quantum adversary gains the ability to derive private keys from exposed public keys.
  - [https://groups.google.com/g/bitcoindev/c/0E1UyyQIUA0](https://groups.google.com/g/bitcoindev/c/0E1UyyQIUA0)

- **BIP 360: Pay to Merkle Root (P2MR)**: A new BIP specifying "Pay to Merkle Root," a transaction output format designed to enhance Bitcoin's scripting capabilities. The proposal was merged in February 2026 as a Draft specification.
  - [https://github.com/bitcoin/bips/pull/1670](https://github.com/bitcoin/bips/pull/1670)

- **BIP 392: Silent Payment Output Script Descriptors**: Introduces a new output descriptor format for Silent Payments (BIP352), proposing `sp()` script expressions with `spscan` and `spspend` key expressions, allowing wallets to represent and manage silent payment keys using a standardized descriptor format.
  - [https://github.com/bitcoin/bips/pull/2047](https://github.com/bitcoin/bips/pull/2047)

- **Two-block reorg at height 941880**: A mining event where Foundry mined two consecutive blocks, causing a reorganization that displaced blocks from AntPool and ViaBTC. Analysis suggests network latency and block propagation timing as contributing factors.
  - [https://bnoc.xyz/t/two-block-reorg-at-height-941880/97](https://bnoc.xyz/t/two-block-reorg-at-height-941880/97)

- **Fuzzor: continuous fuzzing infrastructure**: Experimental continuous fuzzing infrastructure primarily designed to test Bitcoin Core, supporting multiple fuzzing engines (AFL++, libFuzzer, honggfuzz) with automated bug detection, crash deduplication, and coverage analysis.
  - [https://github.com/dergoegge/fuzzor](https://github.com/dergoegge/fuzzor)

- **Want to submit a discussion topic?** Open an issue or PR at [https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io](https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io)
