# Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts

- **Paper**: https://arxiv.org/abs/2604.18473
- **arXiv ID**: 2604.18473v1 (2026-04-20)
- **Authors**: Jacob Morrison, Sanjay Adhikesaven, Akshita Bhagia, Matei Zaharia, Noah A. Smith, Sewon Min
- **Primary affiliations**: University of Washington; University of California, Berkeley; Allen Institute for AI
- **Source**: arXiv (cs.LG)

## Summary
BAR (Branch-Adapt-Route) proposes modular post-training for LLMs by training domain-specific experts independently and composing them with a lightweight Mixture-of-Experts router. This aims to avoid catastrophic forgetting and reduce update cost compared to monolithic retraining.

## Method details
1. Train domain experts independently (math/code/tool/safety).
2. Merge experts into a MoE backbone.
3. Train a lightweight router for task-conditioned expert selection.
4. Update/add experts without retraining every domain.

## Implementation in this folder
`impl/bar_modular_moe_demo.py` provides:
- A toy expert pool (`math`, `code`, `tool`, `safety`, `general`).
- A lightweight router with keyword-conditioned logits and softmax routing.
- A small benchmark showing per-task routing decisions and accuracy.

This is a **research-faithful prototype** (not the original model weights/training stack), useful for understanding modular routing behavior and update mechanics.

## Reproducibility notes
- Python 3.10+
- No third-party dependencies required.
- Run:

```bash
python impl/bar_modular_moe_demo.py
```

## References
- Morrison et al., *Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts*, arXiv:2604.18473, 2026.
