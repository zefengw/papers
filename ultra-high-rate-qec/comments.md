# Critical Notes & Extensions

## Limitations
- Hardware Overhead: While qubit counts are lower, the movement of atoms (reconfiguration) introduces its own noise and latency.
- Decoder Complexity: High-rate QLDPC codes often require more complex decoders (like Belief Propagation) than the simple MWPM used for surface codes.

## Extension Ideas
- **Dynamic Code Switching**: Adapt the code rate dynamically based on the detected noise level of the atom array.
- **Hybrid Architectures**: Combine high-rate QLDPC for storage and surface codes for fast gate operations.
