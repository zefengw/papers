# Fast and accurate AI-based pre-decoders for surface codes

- **Paper**: https://arxiv.org/abs/2604.12841
- **arXiv ID**: 2604.12841
- **Authors**: Christopher Chamberland, Jan Ollé, Muyuan Li, Scott Thornton, Igor Baratta
- **Primary affiliations**: NVIDIA Corporation.
- **Source**: arXiv quant-ph, submitted 2026-04-14

## Why this matters now

Directly tackles real-time quantum error-decoding latency with modular pre-decoding plus downstream global decoding—a near-term FTQC bottleneck.

## Method overview

This folder provides a practical, runnable interpretation of one key implementation idea from the paper and translates it into a lightweight prototype suitable for quick experimentation.

## Reproducibility notes

- Environment: Python 3.10+ (stdlib-only for this demo)
- Run:

```bash
python3 impl/surface_code_predecoder_demo.py
```

- Outputs are deterministic or seeded where relevant.

## Implementation artifacts

- `impl/`: runnable code prototype
- `comments.md`: critical review, limitations, and extension ideas

## Reference

- arXiv abstract page: https://arxiv.org/abs/2604.12841
