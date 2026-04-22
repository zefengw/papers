# TEMPO: Scaling Test-time Training for Large Reasoning Models

- **Paper**: https://arxiv.org/abs/2604.19295
- **arXiv**: 2604.19295v1 (2026-04-21)
- **Authors**: Qingyang Zhang, Xinke Kong, Haitao Wu, Qinghua Hu, Minghao Wu, Baosong Yang, Yu Cheng, Yun Luo, Ganqu Cui, Changqing Zhang
- **Primary affiliations**: Tianjin University, Tongyi Lab (Alibaba Group), The Chinese University of Hong Kong, Shanghai AI Lab
- **Category**: cs.LG

## Summary
TEMPO proposes a scalable test-time training loop for reasoning LLMs by alternating:
1. **Policy refinement** on unlabeled test instances.
2. **Critic recalibration** on a labeled anchor set.

The key claim: without recalibration, reward estimates drift and gains plateau.

## Method details
- Interpret test-time adaptation as an EM-like process.
- E-step-like updates improve policy using pseudo-reward.
- M-step-like updates recalibrate critic with trusted labels.
- Periodic recalibration preserves learning signal quality and diversity.

## Reproducibility notes
`impl/tempo_demo.py` simulates reward drift at test time and compares:
- No recalibration baseline.
- Periodic recalibration strategy (TEMPO-like).

Run:
```bash
python3 impl/tempo_demo.py
```

## References
- arXiv: https://arxiv.org/abs/2604.19295
