# Critical Notes — Flash Boys 2.0

## Strengths
- Early, concrete quantification of MEV and ordering manipulation in production systems.
- Connected microstructure behavior (PGA bidding) to consensus-layer risk.

## Limitations
- Ecosystem evolved quickly (private mempools, PBS/MEV-Boost), so mechanisms shifted.
- A simplified arbitrage model may miss cross-domain MEV and latency engineering details.

## Potential extensions
- Model proposer-builder separation and private orderflow channels.
- Add user slippage impact and welfare metrics.
- Compare mitigation designs: frequent batch auctions, encrypted mempools, fair ordering.
