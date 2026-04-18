# Critical Notes

- The raw term model (4^n) is a worst-case abstraction; real matrices have structure.
- Threshold compression is modeled by a fixed keep-ratio rather than learned/error-bounded truncation.
- Distributed runtime model ignores network heterogeneity and queueing effects.

## Extension Ideas

1. Add matrix-structure-aware Pauli decomposition generator.
2. Track approximation error versus threshold to draw accuracy/throughput Pareto front.
3. Integrate real MPI/CUDA-Q logs to calibrate scheduler overhead.
