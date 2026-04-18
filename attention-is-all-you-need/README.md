# Attention Is All You Need

- **Paper**: https://arxiv.org/abs/1706.03762
- **Authors**: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
- **Primary affiliations**: Google Brain / Google Research (now Google DeepMind), University of Toronto
- **Publication / source**: arXiv:1706.03762v7 (cs.CL, cs.LG), originally submitted 2017-06-12
- **Implementation status**: Runnable attention forward-pass demo

## Summary
Introduces the Transformer architecture: sequence modeling with self-attention and feed-forward blocks, removing recurrence and convolutions.

## Key ideas
- Scaled dot-product attention for stable gradients at larger hidden dimensions.
- Multi-head attention to capture diverse token relations in parallel.
- Positional encodings to preserve order without recurrence.
- Parallelizable training with strong quality/throughput trade-offs.

## Method details in this repository
- `impl/scaled_dot_product_attention_demo.py` computes self-attention for a toy sequence.
- Demonstrates both unmasked attention and causal masking.
- Prints attention weights and output vectors for inspection.

## Reproducibility notes
- Pure Python (standard library only), CPU-only, deterministic values.
- Run: `python3 impl/scaled_dot_product_attention_demo.py`
- This is a pedagogical slice of the paper, not a full WMT reproduction.

## References
- arXiv abstract: https://arxiv.org/abs/1706.03762
- arXiv PDF: https://arxiv.org/pdf/1706.03762.pdf
