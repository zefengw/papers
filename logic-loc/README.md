# LogicLoc: Neurosymbolic Repo-level Code Localization

## Summary
LogicLoc addresses the "Keyword Shortcut" bias in code localization, where models rely on surface-level lexical matches (like file names) rather than structural reasoning. It proposes a neurosymbolic framework that combines LLMs with **Datalog** to perform precise, verifiable localization in large codebases.

## Method Details
- **Keyword-Agnostic Localization**: Shifts focus from lexical matching to structural patterns.
- **Datalog Synthesis**: An LLM synthesizes Datalog programs that describe the structural constraints of the target code (e.g., "Function A calls Function B which is defined in File C").
- **Closed-Loop Workflow**: The Datalog program is executed by a deterministic engine, and results are used to refine the LLM's query via mutation-based feedback.
- **Efficiency**: Offloads structural traversal to Datalog, reducing token usage and latency compared to iterative LLM-only search.

## Reproducibility Notes
The core logic involves representing a codebase as a set of Datalog facts (edges in a call graph) and querying them using a synthesized rule.

## References
- arXiv: 2604.16021v1
