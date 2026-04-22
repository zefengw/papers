# SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language Models

- **Paper**: https://arxiv.org/abs/2604.19638
- **arXiv**: 2604.19638v1 (2026-04-21)
- **Authors**: Josue Torres-Fonseca, Naihao Deng, Yinpei Dai, Shane Storks, Yichi Zhang, Rada Mihalcea, Casey Kennington, Joyce Chai
- **Primary affiliations**: University of Michigan, Boise State University
- **Categories**: cs.AI, cs.CL, cs.RO

## Summary
SafetyALFRED extends embodied evaluation beyond hazard recognition QA. It emphasizes **active mitigation planning** in physically grounded tasks, exposing a key alignment gap between "knowing a hazard" and "actually mitigating it".

## Method details
- Add realistic kitchen hazards to ALFRED-like embodied tasks.
- Evaluate two capabilities separately:
  1. Hazard recognition (QA-like perception).
  2. Safety mitigation success (action planning/execution).
- Report gap as a primary signal.

## Reproducibility notes
`impl/safetyalfred_gap_demo.py` creates a synthetic benchmark with six hazard classes and model profiles, then reports recognition-vs-mitigation gaps and risk-adjusted score.

Run:
```bash
python3 impl/safetyalfred_gap_demo.py
```

## References
- arXiv: https://arxiv.org/abs/2604.19638
- Upstream project: https://github.com/sled-group/SafetyALFRED
