# Comments

## Critical notes
- The key insight is *divergence*, not a single monotonic "bigger is better" story.
- This has immediate implications for eval design: semantic robustness tests and mechanical-copying tests should both be tracked.

## Limitations (in this repo demo)
- Demonstration uses synthetic measurements, not raw benchmark outputs.
- No confidence intervals, cross-family uncertainty, or heteroskedastic modeling.
- Omits prompt-format effects that may alter entrainment estimates.

## Potential extensions
- Add bootstrap confidence intervals for fitted exponents.
- Compare families with mixed-effects models.
- Integrate controlled prompt templates and context corruption experiments.
