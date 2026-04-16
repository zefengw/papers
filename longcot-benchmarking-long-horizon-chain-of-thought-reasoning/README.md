# LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning

- **Paper**: https://arxiv.org/abs/2604.14140v1
- **Field**: AI (reasoning evaluation / long-horizon CoT)
- **Implementation status**: Working toy benchmark implementation

## What this implementation covers

This project implements a **lightweight long-horizon reasoning benchmark** inspired by the paper's central question:
> how does reasoning quality degrade as dependency horizon grows?

We create synthetic recurrence tasks where each step depends on both recent and distant prior steps. Two reasoners are compared:

1. **Short-context reasoner**: keeps only a limited memory window and uses heuristics for missing long-range dependencies.
2. **Planned reasoner**: builds a dependency-aware execution plan and keeps all required state, preserving long-horizon correctness.

## Why this is relevant

LongCoT emphasizes that long-horizon reasoning requires more than local token fluency: it needs robust planning and intermediate-state management. This benchmark isolates exactly that failure mode in a reproducible CPU-only setup.

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

JSON showing, for each horizon bucket:

- exact-match accuracy for short-context vs planned reasoner
- mean absolute error for both methods
- aggregate degradation statistics (drop from shortest to longest horizon)
