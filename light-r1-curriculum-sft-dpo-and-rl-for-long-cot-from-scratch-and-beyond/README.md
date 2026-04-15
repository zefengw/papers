# Light-R1: Curriculum SFT, DPO and RL for Long COT from Scratch and Beyond

- **Paper**: https://arxiv.org/abs/2503.10460v4
- **Field**: AI (Reasoning LLM training)
- **Implementation status**: Working toy implementation (faithful training mechanics, compact scale)

## What this implementation covers

This project implements a compact, executable training pipeline inspired by Light-R1's staged recipe:

1. **Curriculum SFT stage**: learn from easier-to-harder examples.
2. **Preference optimization stage (DPO-style)**: bias policy toward preferred reasoning behavior.
3. **Group-relative RL stage (GRPO-style)**: use group-normalized rewards to stabilize improvements.

Rather than training a full LLM, we use a minimal stochastic policy over reasoning strategies on arithmetic tasks, which keeps the code runnable on CPU in seconds while preserving the algorithmic ideas.

## Why this is relevant

The paper's practical value is in its reproducible, multi-stage recipe for improving reasoning quality under budget constraints. This implementation demonstrates that recipe in an inspectable form.

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

A stage-by-stage report similar to:

- baseline accuracy
- post-curriculum SFT accuracy
- post-DPO accuracy
- post-GRPO accuracy

with final policy parameters and interpretation.
