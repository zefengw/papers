# Comments

## Strengths
- Clear operational criterion (EV sign) for choosing critic usage.
- Practical for unstable sparse-reward regimes common in reasoning post-training.
- Easy to bolt onto existing PPO/GRPO-like loops.

## Limitations
- EV from a single batch can be noisy at small batch sizes.
- Toy assumptions may break under heavy off-policy drift.
- Real training loops need additional safeguards (KL constraints, reward clipping, curriculum).

## Extension ideas
- Smooth gate with hysteresis instead of hard threshold.
- Per-token or per-trajectory EV gating instead of batch-wide decisions.
- Couple EV signal with uncertainty estimates from ensembles.
