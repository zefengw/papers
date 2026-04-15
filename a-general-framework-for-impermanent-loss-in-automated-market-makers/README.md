# A General Framework for Impermanent Loss in Automated Market Makers

- **Paper**: https://arxiv.org/abs/2203.11352v1
- **Field**: Web3 / DeFi (AMM theory)
- **Implementation status**: Working implementation of weighted geometric-mean AMM IL analytics

## What this implementation covers

This project implements a practical analytics toolkit for impermanent loss (IL) in weighted geometric-mean CFMMs (G3M), including:

- post-arbitrage reserve remapping under external price changes,
- closed-form IL computation,
- a sweep utility for scenario analysis,
- validation against the classic constant-product IL formula.

## Why this is relevant

The paper frames IL in a general mathematical lens. This implementation converts that framing into a reusable script for LP risk analysis and strategy exploration.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python run_demo.py
```

## Expected output

- table of IL values across price moves and weight profiles
- constant-product consistency check (numerical error near zero)
