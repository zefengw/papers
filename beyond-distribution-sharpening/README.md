# Beyond Distribution Sharpening: The Importance of Task Rewards

## Summary
This paper investigates whether Reinforcement Learning (RL) in frontier models genuinely teaches new skills or simply "sharpens" the existing distribution of the base model to elicit latent capabilities. The authors compare **Distribution Sharpening** (using RL to move the model closer to a target distribution without explicit task rewards) against **Task-Reward-Based Learning**.

## Method Details
- **Distribution Sharpening**: A paradigm where the model's output distribution is shifted to match a target (e.g., via KL divergence) to increase the probability of "correct-looking" tokens.
- **Task-Reward-Based RL**: Standard RL where the model is optimized based on a reward signal tied to the actual correctness of the task outcome.
- **Finding**: Distribution sharpening is fundamentally unstable and yields limited gains. Incorporating actual task-based reward signals is essential for robust performance improvements.

## Reproducibility Notes
The core idea can be simulated by comparing the convergence of a probability distribution under a "sharpening" objective (maximizing probability of a mode) versus a "reward" objective (maximizing a utility function).

## References
- arXiv: 2604.16259v1
