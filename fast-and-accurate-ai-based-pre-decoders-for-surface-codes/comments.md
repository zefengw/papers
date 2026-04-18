# Critical Notes

- Real surface-code decoding depends on syndrome history over time and circuit-level noise; this toy uses a static 2D snapshot.
- Local cancellation is a heuristic stand-in, not the paper's trained AI pre-decoder.
- Global decoder cost proxy is synthetic and only used for relative comparisons.

## Extension Ideas

1. Move to spacetime syndrome tensors and simulate repeated rounds.
2. Replace heuristic pre-decoder with a small CNN/transformer classifier.
3. Integrate with PyMatching or CUDA-Q workflows for realistic benchmarking.
