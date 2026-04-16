# KindHML: formal verification of smart contracts based on Hennessy-Milner logic

- **Paper**: https://arxiv.org/abs/2604.14038v1
- **Field**: Web3 / Formal Methods / Smart Contract Security
- **Implementation status**: Working toy model checker for HML-style properties

## What this implementation covers

This project provides a compact, runnable **Hennessy-Milner Logic (HML) model checker** over a finite labeled transition system representing an escrow smart contract.

It includes:

- a recursive-descent parser for a useful HML subset (`tt`, `ff`, `!`, `&`, `|`, `<a>φ`, `[a]φ`, atomic propositions)
- model-checking semantics for possibility (`<a>`) and necessity (`[a]`)
- verification on both a secure and a deliberately buggy escrow model

## Why this is relevant

The paper focuses on formal smart-contract verification in process-logic style. This implementation turns that concept into executable checks that can surface safety-property violations caused by illegal transitions.

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

JSON containing:

- formula-by-formula truth values on secure vs buggy contract models
- explicit indication of which safety property is violated in the buggy model
