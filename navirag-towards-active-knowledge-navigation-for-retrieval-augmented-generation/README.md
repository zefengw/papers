# NaviRAG: Towards Active Knowledge Navigation for Retrieval-Augmented Generation

- **Paper**: https://arxiv.org/abs/2604.12766
- **Authors**: Jihao Dai, Dingjun Wu, Yuxuan Chen, Zheni Zeng, Yukun Yan, Zhenghao Liu, Maosong Sun
- **Primary affiliations**: Nanjing University; Northeastern University; Tsinghua University
- **Publication / source**: arXiv:2604.12766v1 (cs.CL), 2026-04-14
- **Implementation status**: Minimal runnable prototype

## Summary
Proposes hierarchical knowledge organization plus iterative, agentic navigation, replacing flat chunk retrieval in classic RAG.

## Why it matters
Important for long-document QA and multi-hop evidence retrieval where fixed top-k retrieval misses useful coarse-to-fine evidence chains.

## Key ideas
- Convert corpus into hierarchical records (topic -> subtopic -> evidence nodes).
- Use an LLM controller to iteratively pick next nodes based on current information gaps.
- Stop when evidence sufficiency criterion is met, then synthesize answer from selected evidence.

## Method details in this repository
- `impl/navirag_demo.py` demonstrates one central mechanism from the paper in an executable, inspectable form.
- The goal is conceptual reproducibility of the method idea, not full benchmark replication.

## Reproducibility notes
- This repo contains a minimal deterministic navigator that follows coarse->fine traversal using lexical gain as a stand-in for LLM policy.
- No external dependencies required; script runs on CPU in seconds.
- To reproduce: `python3 impl/navirag_demo.py`.

## Quick run
```bash
python3 impl/navirag_demo.py
```

## References
- Paper: https://arxiv.org/abs/2604.12766
- PDF: https://arxiv.org/pdf/2604.12766.pdf
