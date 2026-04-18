# Distributed Variational Quantum Linear Solver

- **Paper**: https://arxiv.org/abs/2604.14435
- **arXiv ID**: 2604.14435
- **Authors**: Chao Lu, Pooja Rao, Muralikrishnan Gopalakrishnan Meena, Kalyana Chakaravarthi Gottiparthi
- **Primary affiliations**: Oak Ridge National Laboratory (ORNL) and NVIDIA Corporation.
- **Source**: arXiv quant-ph / cs.DC, submitted 2026-04-15

## Why this matters now

Bridges quantum algorithms with practical multi-GPU/multi-node execution; includes compression strategy for LCU terms and scaling evidence.

## Method overview

This folder provides a practical, runnable interpretation of one key implementation idea from the paper and translates it into a lightweight prototype suitable for quick experimentation.

## Reproducibility notes

- Environment: Python 3.10+ (stdlib-only for this demo)
- Run:

```bash
python3 impl/distributed_vqls_workload_sim.py
```

- Outputs are deterministic or seeded where relevant.

## Implementation artifacts

- `impl/`: runnable code prototype
- `comments.md`: critical review, limitations, and extension ideas

## Reference

- arXiv abstract page: https://arxiv.org/abs/2604.14435
