# Critical Notes — A Quantum Approximate Optimization Algorithm

## Strengths
- Clear hybrid quantum-classical template still central to NISQ optimization research.
- Parameterized depth gives a principled quality-vs-cost trade-off.

## Limitations
- Barren plateaus and local minima can make optimization difficult.
- Hardware noise and connectivity constraints can dominate practical performance.

## Potential extensions
- Add noise models and compare ideal vs noisy expectation values.
- Replace grid search with gradient-free optimizers (CMA-ES, SPSA).
- Benchmark against classical approximation algorithms on matched graph families.
