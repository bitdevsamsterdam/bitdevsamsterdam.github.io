---
layout: post
type: socratic
title: "BitDevs Amsterdam, May 14th, 2026"
meetup: https://www.meetup.com/bitdevs-amsterdam/events/313791527
published: true
---

## BitDevs Amsterdam meeting 028!

It's time for another BitDevs! A big thanks to [Bitonic](https://www.bitonic.nl) for sponsoring us with the meeting space. Drinks will be provided, so please ensure you have some dinner beforehand or bring it along to the seminar.

### Thursday, May 14th, 2026 @ 7PM

Doors open at 6:30PM and we will try to start promptly at 7PM. As a reminder, the ground rules of BitDevs are as follows:

1. No photos, videos, or recordings.
1. [Chatham House Rule](https://en.wikipedia.org/wiki/Chatham_House_Rule): you may
   reiterate the contents of the meeting *without* attribution.

These rules exist so that BitDevs participants can speak freely within the event.

### Agenda

#### Bitcoin Core

- **CVE-2024-52911 disclosure**: A use-after-free bug in Bitcoin Core's script validation that could allow attackers to crash nodes or potentially execute remote code. The flaw involves `PrecomputedTransactionData` being destroyed before the `CCheckQueueControl`, causing background validation threads to access freed memory when processing crafted blocks.
  - [https://bitcoincore.org/en/2026/05/05/disclose-cve-2024-52911/](https://bitcoincore.org/en/2026/05/05/disclose-cve-2024-52911/)

- **Knotzi death march**: A countdown timer page tracking BIP-110 nodes that will eventually be disconnected from the Bitcoin network. Provides background reading and visibility into the node deprecation process.
  - [https://jlopp.github.io/knotzi-death-march/](https://jlopp.github.io/knotzi-death-march/)

- **Slow block propagation and validation on signet**: Measurements showing that slowly-validating blocks on Bitcoin's Signet testnet propagate approximately 160 times slower than normal blocks. Median validation took around 20 seconds compared to 176 milliseconds for standard blocks, highlighting real-world impact of BIP 54's targeted issues.
  - [https://b10c.me/observations/16-slow-block-propagation-validation-signet/](https://b10c.me/observations/16-slow-block-propagation-validation-signet/)

- **ViaBTC joins the BIP 54 compatibility train**: Mainnet observer data showing ViaBTC mining BIP 54-compatible coinbase transactions, adding another major pool to the set of miners signaling practical compatibility with Consensus Cleanup constraints.
  - [https://mainnet.observer/charts/mining-pools-mining-bip54-coinbase/](https://mainnet.observer/charts/mining-pools-mining-bip54-coinbase/)

#### Mining and consensus research

- **Inertial Mining**: A proposed mining protocol that produces Nakamoto's intended single longest chain outcome while constituting a true game-theoretic equilibrium. The authors show that neither selfish mining nor any other deviation is profitable for miners controlling less than half the network's power.
  - [https://arxiv.org/abs/2604.06092](https://arxiv.org/abs/2604.06092)

- **Temporary Power Adjusting Withholding (T-PAW) attack**: A generalized block withholding attack strategy targeting mining pools that improves on the existing PAW attack. The research demonstrates that small miners can achieve up to 22x revenue increases in certain scenarios, exposing a structural weakness in pooled mining.
  - [https://arxiv.org/abs/2604.14135](https://arxiv.org/abs/2604.14135)

#### Post-quantum

- **Localhost Research Post Quantum Cryptography Group**: Localhost Research announces a new PQC group with cryptographers Benedikt Bünz and Dan Boneh to research solutions protecting Bitcoin from future quantum threats. The initiative focuses on conservative hash-based signature schemes and threshold constructions suitable for Bitcoin's operational constraints.
  - [https://lclhost.org/blog/post-quantum-cryptography-group/](https://lclhost.org/blog/post-quantum-cryptography-group/)

- **Avoiding an Unnecessary Quantum Freeze**: Proposes an alternative to automatically freezing quantum-vulnerable coins after a fixed period. Instead, a "canary" address would trigger the freeze only if someone proves a quantum computer exists by spending from it, keeping vulnerable coins spendable in the meantime.
  - [https://www.bitmex.com/blog/Avoiding-An-Unnecessary-Quantum-Freeze](https://www.bitmex.com/blog/Avoiding-An-Unnecessary-Quantum-Freeze)

#### Lightning Network

- **LDK Server**: A fully-functional Lightning node in daemon form, providing an API-first solution for deploying and managing a Lightning Network node. It abstracts over LDK and BDK, exposing a gRPC interface for cross-language integration.
  - [https://spiral.xyz/ldkserver.pdf](https://spiral.xyz/ldkserver.pdf)

- **Onion message jamming in the Lightning Network**: Adversaries can flood the network with onion message spam to degrade service for legitimate users. The vulnerability exists because routing nodes currently forward these messages for free, making large-scale jamming economically trivial while legitimate traffic gets rate-limited.
  - [https://delvingbitcoin.org/t/onion-message-jamming-in-the-lightning-network/2414](https://delvingbitcoin.org/t/onion-message-jamming-in-the-lightning-network/2414)

- **Towards a k-of-n Lightning Network node**: Proposes making multisignature Lightning nodes feasible by removing the shachain requirement from BOLT specifications. True k-of-n security (where k devices must be compromised to steal funds) is currently impossible with shachains, requiring protocol changes and gateway nodes to bridge legacy systems.
  - [https://delvingbitcoin.org/t/towards-a-k-of-n-lightning-network-node/2395](https://delvingbitcoin.org/t/towards-a-k-of-n-lightning-network-node/2395)

- **Simple Taproot Channels (BOLT PR #995)**: An extension BOLT spec for Taproot-based Lightning channels using Schnorr signatures, MuSig2 key aggregation, and Taproot scripts. Establishes the minimal changes needed to upgrade channels while maintaining backward compatibility with existing implementations.
  - [https://github.com/lightning/bolts/pull/995](https://github.com/lightning/bolts/pull/995)

#### Community

- Want to submit a discussion topic? Open an issue or PR at [https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io](https://github.com/bitdevsamsterdam/bitdevsamsterdam.github.io)
