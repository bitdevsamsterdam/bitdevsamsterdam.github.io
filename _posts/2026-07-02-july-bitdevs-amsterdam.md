---
layout: post
type: socratic
title: "BitDevs Amsterdam, July 2, 2026"
published: true
---

## BitDevs Amsterdam meeting 030!

It's time for another BitDevs! A big thanks to [Bitonic](https://www.bitonic.nl) for sponsoring us with the meeting space. Drinks will be provided, so please ensure you have some dinner beforehand or bring it along to the seminar.

### Thursday, July 2nd, 2026 @ 7PM

Doors open at 6:30PM and we will try to start promptly at 7PM. As a reminder, the ground rules of BitDevs are as follows:

1. No photos, videos, or recordings.
1. [Chatham House Rule](https://en.wikipedia.org/wiki/Chatham_House_Rule): you may
   reiterate the contents of the meeting *without* attribution.

These rules exist so that BitDevs participants can speak freely within the event.

### Agenda

#### Bitcoin Core

- **PrivateBroadcast IP leak**: A privacy bug in Bitcoin Core 31.0 where a failed BIP324 v2 handshake retries over v1 without Tor, leaking the sender's IP despite `-privatebroadcast`; fixed in 31.1.
  - [https://bitcoincore.org/en/2026/06/06/privatebroadcast-ip-leak/](https://bitcoincore.org/en/2026/06/06/privatebroadcast-ip-leak/)

#### Post-quantum

- **Public key recovery for EC leaves in P2MR (BIP-360)**: Proposes recovering the public key from the signature instead of revealing it in the witness, shrinking the EC spending path of this post-quantum address scheme from 135 to ~100 bytes.
  - [https://delvingbitcoin.org/t/public-key-recovery-for-ec-leaves-in-p2mr-bip-360/2603](https://delvingbitcoin.org/t/public-key-recovery-for-ec-leaves-in-p2mr-bip-360/2603)

#### Layer 2 and scaling

- **Credible Exit and the Law of Conservation of Blockspace**: Argues that the blockspace needed for users to credibly exit to the base layer imposes a fundamental limit on how many users Bitcoin layers can support trust-minimally.
  - [https://delvingbitcoin.org/t/credible-exit-and-the-law-of-conservation-of-blockspace/2503](https://delvingbitcoin.org/t/credible-exit-and-the-law-of-conservation-of-blockspace/2503)

- **Ark: offchain transaction batching**: A commit-chain protocol where an untrusted operator batches transfers of virtual UTXOs into a near-constant ~200 vB onchain footprint, letting recipients accept payments without pre-locking funds.
  - [https://arxiv.org/abs/2605.20952](https://arxiv.org/abs/2605.20952)

- **Bark now on Bitcoin mainnet**: Second has launched Bark, their self-custodial implementation of the Ark protocol, on mainnet, shipping an SDK and apps spanning Ark, Lightning, and on-chain payments.
  - [https://blog.second.tech/bark-now-on-bitcoin-mainnet/](https://blog.second.tech/bark-now-on-bitcoin-mainnet/)

#### Lightning Network

- **lnd zero-timestamp gossip DoS disclosure**: A validly signed gossip message with timestamp 0 panics and crashes lnd nodes before v0.20.1, which now rejects such messages at parse time.
  - [https://delvingbitcoin.org/t/lnd-zero-timestamp-gossip-dos-disclosure/2621](https://delvingbitcoin.org/t/lnd-zero-timestamp-gossip-dos-disclosure/2621)

- **Fast Neutrino header sync (lnd PR #10552)**: Cuts lnd's Neutrino initial sync from hours to minutes by importing pre-built block and filter headers from files or HTTP before falling back to peer-to-peer sync.
  - [https://github.com/lightningnetwork/lnd/pull/10552](https://github.com/lightningnetwork/lnd/pull/10552)

- **Scaling the Lightning Network with Practical Set Reconciliation**: Replaces inefficient flooding-based gossip with set reconciliation via a new adaptive IBLT scheme, cutting reconciliation from hours to minutes in Core Lightning simulations.
  - [https://ipsit.bu.edu/documents/icbc26.pdf](https://ipsit.bu.edu/documents/icbc26.pdf)

- **LNTest: evaluating Lightning-based botnets**: A containerized Core Lightning testbed for studying botnets that abuse Lightning for command-and-control, which debunks prior D-LNBot claims by showing fragile topologies and linear rather than logarithmic scaling.
  - [https://arxiv.org/abs/2606.12887](https://arxiv.org/abs/2606.12887)

#### Community

- Want to submit a discussion topic? Open an issue or PR at [https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io](https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io)
