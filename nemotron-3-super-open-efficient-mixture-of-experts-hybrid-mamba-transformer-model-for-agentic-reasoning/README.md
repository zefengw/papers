# Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning

- **Paper**: https://arxiv.org/abs/2604.12374
- **arXiv ID**: 2604.12374
- **Authors**: NVIDIA et al. (large multi-author consortium)
- **Primary affiliations**: NVIDIA (primary affiliation listed in manuscript).
- **Source**: arXiv cs.LG / cs.AI / cs.CL, submitted 2026-04-14

## Why this matters now

Open-weight agentic reasoning model emphasizing throughput via hybrid Mamba-Transformer + LatentMoE + native speculative decoding, directly relevant to current efficient-inference race.

## Method overview

This folder provides a practical, runnable interpretation of one key implementation idea from the paper and translates it into a lightweight prototype suitable for quick experimentation.

## Reproducibility notes

- Environment: Python 3.10+ (stdlib-only for this demo)
- Run:

```bash
python3 impl/nemotron_moe_specdecode_demo.py
```

- Outputs are deterministic or seeded where relevant.

## Implementation artifacts

- `impl/`: runnable code prototype
- `comments.md`: critical review, limitations, and extension ideas

## Reference

- arXiv abstract page: https://arxiv.org/abs/2604.12374
