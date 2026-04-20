# Critical Notes & Extensions

## Limitations
- Computational Overhead: Calculating differentiable saliency for every token in a long CoT is expensive.
- Saliency $\neq$ Truth: High attention doesn't always mean the token is "correct" or "logical"; it just means the model relied on it.

## Extension Ideas
- **Multi-head Saliency**: Use different attention heads to identify different types of reasoning (e.g., one for factual retrieval, one for logical deduction).
- **Adversarial Saliency**: Train a "critic" to find reasoning tokens that look salient but are actually misleading, and penalize them.
