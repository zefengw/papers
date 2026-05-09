# arbitrage-and-the-stability-of-amm-price-tracking

**Field**: Web3 (DeFi, AMMs)
**Link**: http://arxiv.org/abs/2605.06060v1

## Summary
This paper studies the stability of Automated Market Makers (AMMs) in tracking reference prices. It models the gap between the reference price and the AMM price as a stochastic tracking error, corrected by arbitrageurs. By analyzing block-level corrections, tracking error ergodicity, transaction costs, and liquidity, the authors quantitatively demonstrate how arbitrage incentives guarantee block-scale stability in DeFi.

## Why it matters
Transitions the core economic intuition of DeFi (arbitrage corrects mispricing) into rigorous mathematical bounds, connecting tracking quality to liquidity and execution constraints.

## Implementation Notes
A full implementation requires a complex blockchain simulation environment. The `impl/` folder contains a quantitative toy simulation of the stochastic tracking error and block-level correction mechanism for a Constant Product AMM, reflecting the paper's core stochastic modeling.