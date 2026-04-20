# Critical Notes & Extensions

## Limitations
- Fixed Drift Classes: The system only protects against drifts that fit into the predefined classes (low-rank, sparse, etc.). An adversary could potentially find a "stealthy" drift that satisfies these but still introduces a backdoor.
- Computational Cost of ZKP: While verification is succinct, generating the ZKP for a large model delta can be slow.

## Extension Ideas
- **Adaptive Drift Policies**: Allow the verifier to set different drift bounds for different layers (e.g., stricter for the embedding layer, looser for the MLP layers).
- **Integration with LoRA**: Since LoRA inherently creates low-rank updates, this framework could become a standard for certifying LoRA adapters.
