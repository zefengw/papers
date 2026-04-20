# AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency

## Summary
AtManRL addresses the "faithfulness" problem in Chain-of-Thought (CoT) reasoning, where a model might provide a correct answer but the reasoning trace doesn't actually reflect the underlying process. The paper proposes using **Differentiable Attention Saliency** as a reward signal within the GRPO framework to encourage the model to generate reasoning traces that genuinely influence the final prediction.

## Method Details
- **Saliency Reward**: Instead of just outcome-based rewards (correct/incorrect), AtManRL identifies tokens in the CoT that are crucial for the final answer using attention masks.
- **Differentiable Attention Manipulation**: It trains an additive attention mask to find the most influential tokens.
- **GRPO Integration**: The saliency reward is combined with correctness rewards to jointly optimize for accuracy and interpretability.

## Reproducibility Notes
The core concept involves calculating a "faithfulness" score based on how much the final answer's probability changes when certain reasoning tokens are masked or emphasized (saliency).

## References
- arXiv: 2604.16158v1
