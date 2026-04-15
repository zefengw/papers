# Token-Efficient RL for LLM Reasoning

- **Paper**: https://arxiv.org/abs/2504.20834v4
- **Field**: AI (RL for reasoning / token-efficient training)
- **Implementation status**: Working toy implementation (full-token REINFORCE vs selective-token updates)

## What this implementation covers

This project provides a runnable simulation of the paper's key idea: **optimize only informative tokens** instead of all tokens.

We train a tiny sequence policy and compare:

- **Full-token policy gradient** (all generated tokens updated)
- **Selective-token policy gradient** (first-mismatch onward updates, inspired by token-level credit assignment)

The environment is a compact arithmetic sequence task so training finishes quickly on CPU while preserving the core credit-assignment mechanism.

## Why this is relevant

The paper's practical contribution is reducing memory/compute pressure in reasoning RL. This toy setup isolates the update-all vs update-selective choice in a way that is easy to inspect.

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

JSON with comparative metrics, including:

- exact-match accuracy for full-token training
- exact-match accuracy for selective-token training
- token-level accuracy for both methods
- number of token updates consumed by each method
