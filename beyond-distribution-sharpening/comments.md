# Critical Notes & Extensions

## Limitations
- The study uses relatively small models (Llama-3.2-3B, Qwen2.5-3B) to analyze the phenomenon. It is unclear if the "sharpening" effect behaves differently in 100B+ parameter models.
- The "target distribution" for sharpening is often derived from a teacher model, which might introduce its own biases.

## Extension Ideas
- **Hybrid approach**: Use distribution sharpening for initial alignment (warm-up) and then switch to task-reward RL for fine-grained skill acquisition.
- **Entropy-regularized RL**: Explore how different entropy coefficients impact the trade-off between sharpening and exploration.
