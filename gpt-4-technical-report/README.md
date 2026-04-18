# GPT-4 Technical Report

- **Paper**: https://arxiv.org/abs/2303.08774
- **Authors**: OpenAI et al.
- **Primary affiliations**: OpenAI
- **Publication / source**: arXiv:2303.08774v6 (cs.CL, cs.AI), 2023-03-15
- **Implementation status**: Runnable evaluation-metrics demo inspired by GPT-4 reporting patterns

## Summary
The GPT-4 report documents a large multimodal model, emphasizing predictable scaling behavior, strong benchmark performance, and alignment/safety evaluation.

## Key ideas
- Capability improves with scale and can be forecast from smaller runs.
- Evaluation should combine capability metrics with reliability/safety checks.
- Post-training alignment materially affects behavior and deployment readiness.

## Method details in this repository
- `impl/reliability_eval_demo.py` implements three practical metrics:
  1. benchmark pass@k estimation,
  2. expected calibration error (ECE),
  3. refusal precision/recall for unsafe prompts.
- Uses toy data to illustrate how capability and safety metrics can be tracked jointly.

## Reproducibility notes
- Pure Python (standard library only), deterministic.
- Run: `python3 impl/reliability_eval_demo.py`
- Focus is evaluation methodology, not model training replication.

## References
- arXiv abstract: https://arxiv.org/abs/2303.08774
- arXiv PDF: https://arxiv.org/pdf/2303.08774.pdf
