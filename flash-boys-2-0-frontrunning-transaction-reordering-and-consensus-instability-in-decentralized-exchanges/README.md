# Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges

- **Paper**: https://arxiv.org/abs/1904.05234
- **Authors**: Philip Daian, Steven Goldfeder, Tyler Kell, Yunqi Li, Xueyuan Zhao, Iddo Bentov, Lorenz Breidenbach, Ari Juels
- **Primary affiliations**: Cornell Tech; IC3 (Initiative for CryptoCurrencies and Contracts)
- **Publication / source**: arXiv:1904.05234v1 (cs.CR, cs.GT), 2019-04-10
- **Implementation status**: Runnable MEV priority gas auction simulation

## Summary
The paper documents frontrunning and transaction reordering in DEX ecosystems, framing miner/extractor incentives as a systemic security issue.

## Key ideas
- Priority Gas Auctions (PGAs) let bots buy ordering advantage.
- Transaction-ordering dependencies create extractable value (MEV).
- MEV can distort consensus incentives and harm ordinary users.

## Method details in this repository
- `impl/mev_priority_gas_auction_sim.py` simulates arbitrage races among bots.
- Compares baseline FIFO ordering vs bid-based PGA ordering.
- Reports extracted value, fees paid, and net bot profit.

## Reproducibility notes
- Pure Python simulation, deterministic random seed.
- Run: `python3 impl/mev_priority_gas_auction_sim.py`
- Not chain-accurate, but captures the core incentive mechanism from the paper.

## References
- arXiv abstract: https://arxiv.org/abs/1904.05234
- arXiv PDF: https://arxiv.org/pdf/1904.05234.pdf
