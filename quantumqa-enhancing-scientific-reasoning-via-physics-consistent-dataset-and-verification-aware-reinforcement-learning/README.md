# QuantumQA: Enhancing Scientific Reasoning via Physics-Consistent Dataset and Verification-Aware Reinforcement Learning

- **Paper**: https://arxiv.org/abs/2604.18176
- **arXiv ID**: 2604.18176v1 (2026-04-20)
- **Authors**: Songxin Qu et al.
- **Primary affiliations**: University of Science and Technology of China (Institute of Advanced Technology + School of Physics); Institute of AI, Hefei Comprehensive National Science Center; Anhui University; National University of Singapore
- **Source**: arXiv (cs.AI, quant-ph)

## Summary
QuantumQA targets scientific reliability in quantum reasoning by combining physically verifiable supervision with semantic scoring and reinforcement optimization.

## Method details
- Build a physics-consistent QA dataset.
- Use deterministic verification for hard constraints.
- Fuse deterministic + semantic rewards in RL (verification-aware reward model).

## Implementation in this folder
`impl/quantumqa_vrm_demo.py` implements:
- Simple quantum-state validity checks (normalization and probability bounds).
- Semantic quality rubric scoring.
- Adaptive reward fusion (deterministic + semantic).
- A mini policy-selection loop over answer candidates.

## Reproducibility notes
- Python 3.10+
- No extra dependencies.

```bash
python impl/quantumqa_vrm_demo.py
```

## References
- Qu et al., *QuantumQA*, arXiv:2604.18176, 2026.
