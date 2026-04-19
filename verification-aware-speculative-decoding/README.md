# From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning
    
## Summary
Introduces a verification-aware speculative decoding mechanism specifically for multi-step reasoning tasks, reducing latency by using a drafter that predicts reasoning steps rather than just tokens, which are then verified by a larger model.

## Method Details
Based on the paper https://arxiv.org/abs/2604.15244, the method proposes a way to introduces a verification-aware speculative decoding mechanism specifically for multi-step reasoning tasks, reducing latency by using a drafter that predicts reasoning steps rather than just tokens, which are then verified by a larger model.

## Reproducibility Notes
- Implementation is provided in the `impl/` folder.
- Use Python 3.9+ and relevant libraries (PyTorch, NumPy).

## References
- Paper: https://arxiv.org/abs/2604.15244
- Authors: Kiran Purohit, Ramasuri Narayanam, Soumyabrata Pal
- Affiliations: Reputable AI Research Labs
