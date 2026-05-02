# Claw-Eval-Live: Live Agent Benchmark

## Summary
Traditional static benchmarks are easy to overfit. Claw-Eval-Live introduces a "live" benchmark for workflow agents that refreshes periodically based on real-world workflow demand signals (e.g., ClawHub skill usage).

## Methodology
- **Signal-to-Task Mapping**: Converts high-demand workflow patterns into executable tasks with local sandboxes and business service mocks.
- **Trace-Based Evaluation**: Instead of just checking final output, the benchmark analyzes execution traces, service state changes, and workspace artifacts.
- **Deterministic Grading**: High reliance on deterministic code-based checks rather than pure LLM-judging.

## References
- arXiv: 2604.28139
- Affiliations: MBZUAI, Tsinghua University, Chinese University of Hong Kong (CUHK).
