# FRESCO: Benchmarking and Optimizing Re-rankers for Evolving Semantic Conflict in Retrieval-Augmented Generation

- **Paper**: https://arxiv.org/abs/2604.14227
- **Authors**: Sohyun An, Hayeon Lee, Shuibenyang Yuan, Chun-cheng Jason Chen, Cho-Jui Hsieh, Vijai Mohan, Alexander Min
- **Primary affiliations**: Meta Superintelligence Labs; UCLA
- **Publication / source**: arXiv:2604.14227v1 (cs.IR/cs.AI), 2026-04-14
- **Implementation status**: Minimal runnable prototype

## Summary
Builds a benchmark for temporal semantic conflict in RAG and shows many rerankers over-prefer semantically rich but outdated evidence.

## Why it matters
Directly addresses production RAG failure mode: stale but fluent sources beating fresher, correct updates.

## Key ideas
- Construct evolving-knowledge test cases from historical revisions (e.g., Wikipedia time slices).
- Measure reranker behavior under conflict between semantic relevance and factual recency.
- Optimize instruction/reranking strategy along Pareto front for evolving vs non-evolving tasks.

## Method details in this repository
- `impl/fresco_reranker_demo.py` demonstrates one central mechanism from the paper in an executable, inspectable form.
- The goal is conceptual reproducibility of the method idea, not full benchmark replication.

## Reproducibility notes
- This repo includes a minimal reranker that compares semantic-only ranking vs recency-aware ranking.
- Demonstrates behavior flip on evolving vs static queries.
- Run: `python3 impl/fresco_reranker_demo.py`.

## Quick run
```bash
python3 impl/fresco_reranker_demo.py
```

## References
- Paper: https://arxiv.org/abs/2604.14227
- PDF: https://arxiv.org/pdf/2604.14227.pdf
