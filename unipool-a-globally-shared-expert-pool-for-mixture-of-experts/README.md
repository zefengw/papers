# UniPool: A Globally Shared Expert Pool for Mixture-of-Experts

## Why it matters
UniPool challenges the rigid per-layer allocation of parameters in traditional MoE systems by moving all experts to a global shared pool. This decouples expert parameter growth from depth scaling, drastically improving efficiency at sub-linear budget growth.

## Core Setup
This implementation provides a functionally equivalent PyTorch module demonstrating continuous state-sharing `UniPool` routing vs. traditional isolated `LayerMoE` routing.

## Details
In traditional MoE (e.g. Mixtral), Layer 1 has 8 experts distinct from Layer 2's 8 experts. 
In UniPool, the network allocates a global pool of $N$ experts. All layers route into this shared array, utilizing the full pool-level auxiliary loss described by the paper to prevent expert collapse.

## Usage
Run the comparative script to observe parameter counts and forwarding mechanisms.
```
pip install torch
python unipool.py
```
