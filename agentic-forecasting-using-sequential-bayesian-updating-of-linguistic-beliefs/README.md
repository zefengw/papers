# Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs

- **Paper**: https://arxiv.org/abs/2604.18576
- **arXiv ID**: 2604.18576v1 (2026-04-20)
- **Author**: Kevin Murphy
- **Primary affiliation**: University of British Columbia, Department of Computer Science
- **Source**: arXiv (cs.AI)

## Summary
The BLF system combines iterative evidence gathering with Bayesian updates over a structured linguistic belief state, then applies trial aggregation and calibration to improve forecasting robustness.

## Method details
- Sequential Bayesian updates in log-odds space.
- Multi-trial aggregation with shrinkage toward prior.
- Hierarchical calibration (Platt-style) for probability correction.

## Implementation in this folder
`impl/blf_agentic_forecasting_demo.py` includes:
- Bayesian evidence accumulation for binary forecasts.
- K-trial aggregation with shrinkage.
- A simple calibration step.
- End-to-end toy benchmark reporting Brier score.

## Reproducibility notes
- Python 3.10+
- No extra packages.

```bash
python impl/blf_agentic_forecasting_demo.py
```

## References
- Murphy, *Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs*, arXiv:2604.18576, 2026.
