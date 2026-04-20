# Critical Notes & Extensions

## Limitations
- Latency: Multi-turn verification is significantly slower than a single-pass reward model.
- Agent Loops: There is a risk of agents getting stuck in "agreement loops" where they confirm each other's errors.

## Extension Ideas
- **Cross-Model Verifiers**: Use different model architectures for the Forward and Backward agents to reduce correlated errors.
- **Dynamic Verifier Depth**: Adjust the number of verification turns based on the uncertainty of the initial reward estimate.
