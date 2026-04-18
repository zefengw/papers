# A Quantum Approximate Optimization Algorithm

- **Paper**: https://arxiv.org/abs/1411.4028
- **Authors**: Edward Farhi, Jeffrey Goldstone, Sam Gutmann
- **Primary affiliations**: Massachusetts Institute of Technology (MIT), Center for Theoretical Physics
- **Publication / source**: arXiv:1411.4028v1 (quant-ph), 2014-11-14
- **Implementation status**: Runnable p=1 QAOA simulation for MaxCut on a 3-node graph

## Summary
QAOA introduced a parameterized quantum circuit family for approximate combinatorial optimization, balancing expressivity (depth) with implementability.

## Key ideas
- Alternate problem Hamiltonian and mixer Hamiltonian layers.
- Optimize layer parameters classically.
- Trade quantum circuit depth for solution quality.

## Method details in this repository
- `impl/qaoa_maxcut_demo.py` simulates p=1 QAOA on a triangle graph.
- Performs a small grid search over (gamma, beta).
- Reports best expected cut value and high-probability bitstrings.

## Reproducibility notes
- Pure Python statevector simulation, no external libraries.
- Run: `python3 impl/qaoa_maxcut_demo.py`
- This is a tiny demonstration; scaling to larger graphs needs optimized simulators/hardware.

## References
- arXiv abstract: https://arxiv.org/abs/1411.4028
- arXiv PDF: https://arxiv.org/pdf/1411.4028.pdf
