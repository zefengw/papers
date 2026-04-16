# TIP: Token Importance in On-Policy Distillation

- **Paper**: https://arxiv.org/abs/2604.14084v1
- **Field**: AI (LLM distillation / RL-style on-policy training)
- **Implementation status**: Working toy implementation

## What this implementation covers

This project implements a compact simulation of **on-policy distillation** and compares:

1. **Uniform token weighting** (all token positions contribute equally)
2. **TIP-style weighting** (higher weight for tokens where student behavior diverges from teacher confidence)

The task is two-digit arithmetic generation, which keeps runtime short while preserving token-level supervision dynamics.

## Why this is relevant

The paper's key intuition is that not all tokens are equally informative during on-policy updates. Weighting updates by token importance can reduce wasted gradient effort and improve learning efficiency.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python3 run_demo.py
```

## Expected output

JSON including:

- exact and token-level accuracy for uniform vs TIP-style distillation
- KL divergence to teacher policy
- average per-step token importance used by TIP
