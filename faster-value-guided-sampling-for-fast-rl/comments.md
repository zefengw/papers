# Comments

## Strengths
- Directly targets a practical bottleneck: inference/training compute.
- Compatible with existing diffusion-based or generative policy pipelines.
- Good fit for long-horizon control where candidate branching is expensive.

## Limitations
- Value estimator quality is crucial; poor estimates can over-prune.
- Hyperparameters (prune ratio, step timing) may be task-sensitive.
- Real systems need calibration under OOD states.

## Extension ideas
- Uncertainty-aware pruning with conservative fallback.
- Adaptive prune ratio based on value spread.
- Joint objective balancing speedup and regret.
