# MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval

- **Paper**: https://arxiv.org/abs/2604.18584
- **arXiv ID**: 2604.18584v1 (2026-04-20)
- **Authors**: Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman, Antonio Torralba
- **Primary affiliations**: MIT; KAUST; HUMAIN
- **Source info**: arXiv (cs.AI/cs.DL/cs.IR/cs.LG), comment indicates ICLR 2026

## Summary
MathNet introduces a large multilingual, multimodal Olympiad-style benchmark spanning many countries/languages and supporting three tasks: problem solving, math-aware retrieval, and retrieval-augmented solving.

## Method details
- Curated math dataset with solved problems.
- Retrieval benchmark for equivalent/related problems.
- Evaluation across standalone generation and retrieval-augmented generation.

## Implementation in this folder
`impl/mathnet_retrieval_rag_demo.py` includes:
- A compact multilingual toy MathNet-like corpus.
- A simple retrieval model (character trigram TF weighting).
- Retrieval evaluation (`recall@k`).
- A tiny retrieval-augmented solver to demonstrate quality sensitivity to retrieval.

## Reproducibility notes
- Python 3.10+
- No extra dependencies.

```bash
python impl/mathnet_retrieval_rag_demo.py
```

## References
- Alshammari et al., *MathNet*, arXiv:2604.18584, 2026.
