# Critical Notes

- Uses synthetic data and handcrafted pseudo-text risk scores; no real blockchain graph extraction.
- LLM summary generation is emulated by one scalar (`summary_risk`) instead of real prompt outputs.
- Evaluation metrics are illustrative and not directly comparable to reported KS/F1 in paper.

## Extension Ideas

1. Add chain-specific feature encoders (EVM, UTXO, account-based non-EVM).
2. Replace pseudo-text scalar with actual LLM-generated evidence embeddings.
3. Evaluate zero-shot transfer across held-out chain domains.
