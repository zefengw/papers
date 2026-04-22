# EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training

- **Paper**: https://arxiv.org/abs/2604.19485
- **arXiv**: 2604.19485v1 (2026-04-21)
- **Authors**: Chengjun Pan, Shichun Liu, Jiahang Lin, Dingwei Zhu, Jiazheng Zhang, Shihan Dou, Songyang Gao, Zhenhua Han, Binghai Wang, Rui Zheng, Xuanjing Huang, Tao Gui, Yansong Feng
- **Primary affiliations**: Peking University, Fudan University, Shanghai AI Lab
- **Categories**: cs.LG, cs.AI, cs.CL

## Summary
EVPO addresses a core post-training RL dilemma for LLMs: when to trust a learned critic baseline versus a critic-free baseline (e.g., GRPO-style batch mean). The paper derives a practical switching criterion from **explained variance (EV)** and shows that critic usage should be disabled whenever EV is non-positive.

## Method details
- Compute batch-level explained variance of critic estimates relative to returns.
- If EV > 0, use critic-based advantage estimation.
- If EV <= 0, switch to critic-free baseline (batch-mean style).
- This produces an adaptive optimizer that tracks critic quality over training.

## Reproducibility notes
This repo contains a toy rollout simulator that:
1. Simulates actor-critic training epochs with gradually improving critic quality.
2. Computes EV and compares advantage variance across two baselines.
3. Applies EVPO gating and reports variance reduction and gate decisions.

Run:
```bash
python3 impl/evpo_demo.py
```

## References
- arXiv: https://arxiv.org/abs/2604.19485
- (Semantic Scholar metadata attempted during briefing; rate-limited for many papers)
