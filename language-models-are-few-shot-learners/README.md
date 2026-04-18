# Language Models are Few-Shot Learners

- **Paper**: https://arxiv.org/abs/2005.14165
- **Authors**: Tom B. Brown et al. (OpenAI)
- **Primary affiliations**: OpenAI
- **Publication / source**: arXiv:2005.14165v4 (cs.CL), 2020-05-28
- **Implementation status**: Runnable in-context classification prototype (no gradient updates)

## Summary
GPT-3 showed that scaling autoregressive language models enables strong few-shot performance via prompting alone, reducing reliance on task-specific fine-tuning.

## Key ideas
- Massive scale (175B parameters) substantially improves in-context learning.
- Unified next-token objective supports many tasks through prompt formatting.
- Few-shot prompting can approach or match prior fine-tuned baselines on several tasks.

## Method details in this repository
- `impl/in_context_learning_demo.py` simulates no-update task adaptation.
- Uses a few-shot support set and token-overlap similarity to classify new inputs.
- Demonstrates "task adaptation by context" rather than parameter updates.

## Reproducibility notes
- Pure Python (standard library only), deterministic output.
- Run: `python3 impl/in_context_learning_demo.py`
- This is conceptual: it mirrors the few-shot protocol idea, not GPT-3 scale.

## References
- arXiv abstract: https://arxiv.org/abs/2005.14165
- arXiv PDF: https://arxiv.org/pdf/2005.14165.pdf
