# Learning error suppression strategies for dynamic quantum circuits

- **Paper**: https://arxiv.org/abs/2604.18734
- **arXiv**: 2604.18734v1 (2026-04-20)
- **Authors**: Christopher Tong, Liran Shirizly, Edward H. Chen, Derek S. Wang, Bibek Pokharel
- **Primary affiliations**: Princeton University, MIT, IBM Quantum, Microsoft Discovery & Quantum
- **Category**: quant-ph

## Summary
The paper proposes empirically learned dynamical decoupling (DD) strategies tailored to dynamic quantum circuits with mid-circuit measurement/feedforward. Learned schedules outperform fixed theoretical templates under realistic hardware noise.

## Method details
- Partition dynamic circuits into subintervals/subregisters.
- Learn DD pulse patterns per interval using measured outcomes.
- Optimize for reduced error rates under dynamic-operation noise.

## Reproducibility notes
`impl/dynamic_dd_learning_demo.py` simulates interval-wise noise and compares:
- Fixed DD template.
- Learned per-interval DD policy via local search.

Run:
```bash
python3 impl/dynamic_dd_learning_demo.py
```

## References
- arXiv: https://arxiv.org/abs/2604.18734
