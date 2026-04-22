# Comments

## Strengths
- Targets a key near-term pain point for dynamic circuits.
- Empirical optimization aligns with hardware-specific noise reality.
- Direct relevance to fault-tolerant building blocks.

## Limitations
- Learned schedules may overfit hardware calibration state.
- Search cost can grow with interval/register granularity.
- Transferability across backends is uncertain.

## Extension ideas
- Bayesian optimization over pulse sequence space.
- Multi-objective optimization (error + latency).
- Cross-device transfer with meta-learned initialization.
