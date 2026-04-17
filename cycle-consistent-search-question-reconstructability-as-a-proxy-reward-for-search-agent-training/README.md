# Cycle-Consistent Search: Question Reconstructability as a Proxy Reward for Search Agent Training

- **Paper**: https://arxiv.org/abs/2604.12967
- **Authors**: Sohyun An, Shuibenyang Yuan, Hayeon Lee, Cho-Jui Hsieh, Alexander Min
- **Primary affiliations**: Meta Superintelligence Labs; UCLA
- **Publication / source**: arXiv:2604.12967v1 (cs.AI), 2026-04-14
- **Implementation status**: Minimal runnable prototype

## Summary
Introduces supervision-free reward design for search agents: good trajectories should preserve enough information to reconstruct the original question.

## Why it matters
Reduces dependence on expensive gold answers and labels, enabling larger-scale RL for search/reasoning agents.

## Key ideas
- Define cycle objective: question -> trajectory -> reconstructed question.
- Use reconstructability score as reward proxy for trajectory quality.
- Apply bottlenecks (e.g., masking named entities and removing direct answer strings) to prevent reward hacking via leakage.

## Method details in this repository
- `impl/cycle_consistent_search_demo.py` demonstrates one central mechanism from the paper in an executable, inspectable form.
- The goal is conceptual reproducibility of the method idea, not full benchmark replication.

## Reproducibility notes
- This repo includes a toy cycle-consistency reward calculator contrasting informative vs noisy trajectories.
- Implements leakage penalty with masked entities and overlap-based reconstruction score.
- Run: `python3 impl/cycle_consistent_search_demo.py`.

## Quick run
```bash
python3 impl/cycle_consistent_search_demo.py
```

## References
- Paper: https://arxiv.org/abs/2604.12967
- PDF: https://arxiv.org/pdf/2604.12967.pdf
