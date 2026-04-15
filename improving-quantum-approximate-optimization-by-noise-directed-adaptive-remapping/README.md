# Improving Quantum Approximate Optimization by Noise-Directed Adaptive Remapping

- **Paper**: https://arxiv.org/abs/2404.01412v3
- **Field**: Quantum (QAOA under noise)
- **Implementation status**: Working approximation/simulation of NDAR behavior

## What this implementation covers

The paper introduces NDAR: use gauge/remapping steps to turn a hardware noise attractor from a liability into a search bias.

This implementation provides a fully runnable simulator that includes:

- MaxCut objective on random weighted graphs,
- noisy QAOA-like sampler with a fixed attractor,
- baseline p=1-style sampling,
- iterative NDAR remapping loop that re-targets attractor mapping.

## Why this is an approximation

Real hardware pulse-level/noise physics is not fully reproducible from paper-level details alone in a lightweight script. This code captures the **algorithmic mechanism** (adaptive remapping against a persistent attractor), which is the core practical insight.

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

- baseline and NDAR best cut values
- approximation ratios versus optimum
- per-iteration NDAR progress table
