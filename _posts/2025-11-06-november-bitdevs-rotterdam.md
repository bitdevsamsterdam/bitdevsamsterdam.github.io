---
layout: post
type: socratic
title: "BitDevs Rotterdam, November 6, 2025"
meetup: https://www.meetup.com/bitdevs-amsterdam/events/310124538
published: true
---

## BitDevs Rotterdam meeting 023!

It's time for another BitDevs! A big thanks to [Blockrise](https://www.blockrise.com/nl) for sponsoring us with the meeting space. Drinks will be provided, so please ensure you have some dinner beforehand or bring it along to the seminar.

### Thursday, November 6th, 2025 @ 7PM

Doors open at 6:30PM and we will try to start promptly at 7PM. As a reminder, the ground rules of BitDevs are as follows:

1. No photos, videos, or recordings.
1. [Chatham House Rule](https://en.wikipedia.org/wiki/Chatham_House_Rule): you may
   reiterate the contents of the meeting *without* attribution.

These rules exist so that BitDevs participants can speak freely within the event.

# Agenda

This month's agenda is inspired by the lightning++ conference in Berlin that took place earlier in October. Unfortunately individial videos corresponding to specific talks have not yet been uploaded, and also any recordings of the secondary stage are not uploaded. That means that reading material remains in text form.

- **RGB on lightning**: bringing RGB assets on the LN level by pulling the assets in the channel via the op_return field
   - [lightning++ Talk description](https://btcplusplus.dev/conf/berlin25/talks#b25_rgb)
   - [RGB LN docs](https://docs.rgb.info/rgb-over-lightning-network/lightning-network-compatibility)
- **Spark**: a new solution to batching payments with interesting trust assumptions/guarantees
   - [Spark docs TLDR](https://docs.spark.money/learn/tldr)
   - [Spark docs Technical Definitions](https://docs.spark.money/learn/technical-definitions)
- **Gossip v2: path to minisketch**: Current state of lightning gossip and how minisketch can improve it
   - [Gossip Observer repository](https://github.com/jharveyb/gossip_observer)
   - [Bitcoin Ops: Minisketch](https://bitcoinops.org/en/topics/minisketch/)
- **Lightning's "toxic" waste problem**: In the long term of running a lightning node you have to consider  your own storage as an attack vector on privacy -- you keep track of everything you ever sent/received or forwarded
   - [lightning++ Talk description](https://btcplusplus.dev/conf/berlin25/talks#b25_waste)
   - [Related LND issue](https://github.com/lightningnetwork/lnd/issues/9963)
   - [Pull Request doc explaining this in-depth](https://github.com/lightningnetwork/lnd/blob/017299fe6f3aec3d8c7ece84c383a47da59862f0/docs/forwarding_history_privacy.md)
- **State of Lightning Privacy**: One of the strongest aspects of lightning is the privacy model. How well does it hold and how hard is it for an attacker to gain any information related to identifying the actors within the system.
   - [arxiv: Research Paper](https://arxiv.org/abs/2006.12143)
   - [Stackernews post with older video](https://stacker.news/items/1012159)
