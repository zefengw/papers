# Critical Notes — Attention Is All You Need

## Strengths
- Architectural simplification (attention-only) unlocked major parallel training gains.
- Became the foundation for modern LLMs, multimodal models, and long-context work.

## Limitations
- Quadratic attention cost in sequence length remains expensive for long contexts.
- Original positional encoding can underperform relative to modern rotary/relative methods.

## Potential extensions
- Swap dense attention with sparse/linear variants for long inputs.
- Compare learned vs rotary positional encodings in the demo.
- Add multi-head decomposition and residual/LayerNorm blocks to move toward a tiny full Transformer.
