# Comments

## Critical notes
- The paper's core contribution is *active* navigation over hierarchical knowledge, which can reduce retrieval myopia seen in flat chunk pipelines.
- A real implementation depends heavily on traversal policy quality; weak policy can wander and increase latency.

## Limitations (in this repo demo)
- Uses lexical overlap instead of an LLM planner and learned retrieval policy.
- No uncertainty calibration or explicit stop criterion learning.
- No benchmark integration yet (e.g., long-document QA suites).

## Potential extensions
- Replace lexical node scoring with dense retrieval + reranker.
- Add budgeted search (token/time constraints) and measure utility-per-step.
- Add trajectory logging and offline policy optimization for navigation decisions.
