# Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes

## Summary
Crab is a runtime system designed for AI agents that need to operate in sandboxed environments (like browsers, code execution shells). It focuses on making checkpointing and restoring agent state "semantics-aware" to speed up development and evaluation.

## Methodology
- **Semantic Checkpointing**: Instead of just freezing raw system memory, Crab identifies high-level "semantic" checkpoints (e.g., successful service login, file creation).
- **Restore Logic**: Allows rolling back an agent to a specific stable state without re-executing long, expensive tool-use chains.
- **Interoperability**: Designed to work with standard container runtimes but adds a layer of agent-specific observability.

## References
- arXiv: 2604.28138
- Affiliations: UC Berkeley.
