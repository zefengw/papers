# Sequence vs. Simultaneous Entanglement Swapping under Optimal Link-Layer Control

**Link:** http://arxiv.org/abs/2605.04047v1
**Field:** Quantum (Networking)
**Relevance:** Provides a direct comparison of entanglement swapping paradigms, critical for near-term scalable quantum network architecture.

## Summary
Connection-less, packet-switched quantum network architectures distribute entanglement across multi-hop paths through sequential entanglement swapping, in which each node acts on purely local state information. The architectural advantages over the connection-oriented alternative -- simultaneous SWAP-ASAP -- are compelling, but sequential swapping holds partial chains in intermediate buffers between successive swaps, exposing them to memory decoherence in a way simultaneous SWAP-ASAP avoids by design. We present a proof-of-principle study at fixed chain length n = 4 in which each elementary link is governed by a fixed reinforcement-learning policy optimizing the secret-key rate of the six-state protocol, leaving the network-layer protocol as the sole independent variable. Sweeping the network-layer memory coherence time over four orders of magnitude reveals a clear regime structure governed by the dimensionless ratio of coherence time to heralding latency. Simultaneous SWAP-ASAP delivers a constant rate across the full sweep. Sequential swapping, by contrast, collapses to zero end-to-end deliveries below a critical threshold, and begins recovering later. It remains limited by the simultaneous rate, which it saturates only at the relaxed end of the sweep. These results suggest that the connection-less penalty is a near-term phenomenon tied to present-day memory coherence rather than a fundamental property of sequential swapping.

## Implementation Status
**Status:** Approximation

### Reason
Full implementation requires specialized training setups, hardware, or access to the specific datasets/models mentioned in the paper, which are not currently available or feasible to run in a short timeframe. 
We provide a conceptual scaffold reflecting the core mechanism discussed.
