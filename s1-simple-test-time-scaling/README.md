# s1: Simple Test-Time Scaling

## Summary
Building on the "OpenR1" and "Strawberry" trends, s1 demonstrates that significant reasoning performance gains can be achieved through simple test-time scaling methods (like Budget-Force search) without necessarily using complex RL if the base model is strong enough.

## Methodology
- **Test-Time Scaling**: Allocating more compute at inference time via multiple rollouts and a "best-of-N" verifier or consensus mechanism.
- **Budget-Force Search**: Iteratively refining solutions within a fixed token/time budget.
- **Performance**: Matches or exceeds the performance of much larger models that lack test-time compute scaling.

## References
- arXiv: 2501.12948 (Highly influential recent work in Reasoning Models)
- Affiliations: Stanford University.
