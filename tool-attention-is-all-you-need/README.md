# Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading

## Summary
This paper introduces a dynamic gating mechanism for Large Language Model (LLM) agents to efficiently manage large scales of external tools (MCP/Model Context Protocol). It addresses the "Tools Tax"—the performance and cost overhead of injecting massive tool schemas into the model's context for every turn.

## Key Methods
- **Dynamic Tool Gating**: A lightweight relevance-based attention pass to select top-k tools.
- **Lazy Schema Loading**: Injecting tool definitions on-demand post-selection.
- **MCP Optimization**: Reducing per-turn token costs by up to 90%.

## Reproducibility
The implementation provides a simplified simulation of the gating mechanism using embeddings to select relevant tools from a registry without full context injection.

## References
Anuj Sadani, Deepak Kumar. "Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows". arXiv:2604.21816, 2026.
