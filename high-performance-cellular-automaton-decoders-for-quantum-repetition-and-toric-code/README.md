# High-Performance Cellular Automaton Decoders for Quantum Repetition and Toric Code

## Summary
Proposes a scalable decoding architecture using cellular automata (CA) for real-time error correction in large-scale quantum computers. Unlike centralized decoders (MWPM), CA decoders are local and fully parallelizable, suitable for FPGA/ASIC implementation near the quantum processor.

## Key Methods
- **Local Decoding Rules**: Each cell in the CA updates its state based only on its immediate neighbors and local syndromes.
- **Toric Code Adaptation**: Extending the CA approach from 1D repetition codes to 2D periodic lattices.
- **Performance**: Achieving low logical error rates with O(1) per-cell complexity.

## References
Don Winter, Thiago L. M. Guedes, Markus Müller. arXiv:2604.21866, 2026.
