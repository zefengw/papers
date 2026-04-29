# s1 Simple Test-Time Scaling

## Summary
Achieves competitive reasoning via a 1k high-quality dataset (s1K) and 'budget forcing' where the thinking process is either terminated or extended using 'Wait' injections at test-time.

## Method Details
- **Authors**: Niklas Muennighoff, et al.
- **Published**: 2025-01-31
- **arXiv ID**: [2501.19393v3](https://arxiv.org/abs/2501.19393v3)

## Reproducibility Notes
Uses Qwen2.5-32B base. Budget forcing happens at the logit suppression layer during inference.

## References
- https://arxiv.org/abs/2501.19393v3
