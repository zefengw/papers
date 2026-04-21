# Comments: Blockspace Under Pressure

## Critical notes
- Spam-MEV can inflate fee pressure while adding little user-facing utility.
- Block-level decomposition (spam vs organic flows) is operationally useful for sequencer policy design.

## Limitations
- This prototype uses synthetic data, not live chain traces.
- Mitigation rule is intentionally simple and may create false positives.

## Extension ideas
1. Fit spam classifier from real mempool/ledger features.
2. Evaluate policy under adaptive adversaries.
3. Add welfare metrics (latency, failed txs, user cost).
