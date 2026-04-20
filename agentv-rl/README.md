# AgentV-RL: Scaling Reward Modeling with Agentic Verifier

## Summary
AgentV-RL introduces an **Agentic Verifier** to improve reward modeling for complex reasoning tasks. Instead of a single-pass reward model (ORM), it uses a multi-turn, tool-augmented deliberative process involving **Forward** and **Backward** verification agents to ensure the reliability of solutions.

## Method Details
- **Forward Agent**: Traces the solution from the premises to the conclusion, checking each step for logical consistency.
- **Backward Agent**: Re-checks the conclusion by working backward to see if the premises necessarily lead to it.
- **AgentV-RL**: Uses reinforcement learning to allow the verifier to autonomously interleave tool-use (e.g., code execution, search) with internal reasoning.
- **Test-Time Scaling (TTS)**: The agentic nature allows for better performance under both parallel and sequential sampling.

## Reproducibility Notes
The system can be implemented as a dual-agent loop where a "Solution" is passed to both a Forward and Backward verifier. The final reward is a function of both agents' agreement and their internal confidence.

## References
- arXiv: 2604.16004v1
