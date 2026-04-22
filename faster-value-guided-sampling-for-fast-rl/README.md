# FASTER: Value-Guided Sampling for Fast RL

- **Paper**: https://arxiv.org/abs/2604.19730
- **arXiv**: 2604.19730v1 (2026-04-21)
- **Authors**: Perry Dong, Alexander Swerdlow, Dorsa Sadigh, Chelsea Finn
- **Primary affiliation**: Stanford University
- **Categories**: cs.LG, cs.AI

## Summary
FASTER reduces test-time scaling cost in generative RL by pruning low-value action candidates earlier in denoising. It approximates full best-of-N sampling quality with substantially lower compute.

## Method details
- Treat denoising and candidate filtering as an MDP in latent action space.
- Learn/use a value estimate to keep promising candidates and drop weak ones early.
- Preserve performance while cutting candidate processing cost.

## Reproducibility notes
`impl/faster_demo.py` simulates a denoising stack with candidate values and compares:
- Full best-of-N sampling.
- Value-guided early pruning (FASTER-like).

Run:
```bash
python3 impl/faster_demo.py
```

## References
- arXiv: https://arxiv.org/abs/2604.19730
- Code link from paper: https://github.com/alexanderswerdlow/faster
