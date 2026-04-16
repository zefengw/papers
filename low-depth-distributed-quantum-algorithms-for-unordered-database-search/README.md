# Low Depth Distributed Quantum Algorithms for Unordered Database Search

- **Paper**: https://arxiv.org/abs/2604.14081v1
- **Field**: Quantum Computing (distributed search / depth reduction)
- **Implementation status**: Working toy simulator

## What this implementation covers

This project implements a small state-vector simulation to compare:

1. **Centralized Grover search** over the full database
2. **Distributed search** where the database is sharded and Grover runs in parallel on each shard

The implementation reports both success rates and a hardware-agnostic depth proxy to illustrate the depth-vs-success tradeoff discussed in low-depth distributed approaches.

## Why this is relevant

The paper studies reducing circuit depth for near-term hardware. Sharding and parallel local search can reduce wall-clock depth, even if per-shot success must be balanced via iteration count and verification.

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

- centralized Grover success probability
- distributed success probability
- depth proxy for centralized vs distributed execution
- depth reduction ratio under parallel shard execution
