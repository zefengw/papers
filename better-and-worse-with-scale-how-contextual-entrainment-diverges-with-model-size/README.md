# Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size

- **Paper**: https://arxiv.org/abs/2604.13275
- **Authors**: Dikshant Kukreja, Kshitij Sah, Gautam Gupta, Avinash Anand, Rajiv Ratn Shah, Zhengkui Wang, Aik Beng Ng, Erik Cambria
- **Primary affiliations**: IIIT Delhi; NVIDIA; Nanyang Technological University; Singapore Institute of Technology
- **Publication / source**: arXiv:2604.13275v1 (cs.CL/cs.LG), 2026-04-14
- **Implementation status**: Minimal runnable prototype

## Summary
Derives scaling-law behavior for contextual entrainment, showing model scaling can reduce semantic misinformation susceptibility while increasing non-semantic copying.

## Why it matters
Challenges the assumption that larger models uniformly improve context handling; useful for prompt design and guardrail design at scale.

## Key ideas
- Define contextual entrainment metrics across semantic vs non-semantic contexts.
- Measure across model scales (Cerebras-GPT and Pythia families).
- Fit power-law trends and compare opposite-direction exponents.

## Method details in this repository
- `impl/contextual_entrainment_scaling_demo.py` demonstrates one central mechanism from the paper in an executable, inspectable form.
- The goal is conceptual reproducibility of the method idea, not full benchmark replication.

## Reproducibility notes
- This repo includes a compact log-log power-law fitter and trend extrapolator.
- Demonstrates opposite exponents for semantic vs non-semantic entrainment curves using toy measurements.
- Run: `python3 impl/contextual_entrainment_scaling_demo.py`.

## Quick run
```bash
python3 impl/contextual_entrainment_scaling_demo.py
```

## References
- Paper: https://arxiv.org/abs/2604.13275
- PDF: https://arxiv.org/pdf/2604.13275.pdf
