# An Engineering Journey Training Large Language Models at Scale on Alps: The Apertus Experience

- **Paper**: https://arxiv.org/abs/2604.12973
- **arXiv ID**: 2604.12973
- **Authors**: Jonathan Coles, Stefano Schuppli, Lukas Drescher, et al.
- **Primary affiliations**: Swiss National Supercomputing Centre (CSCS), NVIDIA, HPE, EPFL, ETH Zurich.
- **Source**: arXiv cs.DC, submitted 2026-04-14

## Why this matters now

Rare transparent report of 70B-scale academic training operations on GH200-class HPC systems; highly actionable for sovereign/open model ops teams.

## Method overview

This folder provides a practical, runnable interpretation of one key implementation idea from the paper and translates it into a lightweight prototype suitable for quick experimentation.

## Reproducibility notes

- Environment: Python 3.10+ (stdlib-only for this demo)
- Run:

```bash
python3 impl/alps_training_capacity_planner.py
```

- Outputs are deterministic or seeded where relevant.

## Implementation artifacts

- `impl/`: runnable code prototype
- `comments.md`: critical review, limitations, and extension ideas

## Reference

- arXiv abstract page: https://arxiv.org/abs/2604.12973
