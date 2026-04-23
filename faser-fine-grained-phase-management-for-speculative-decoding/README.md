# FASER: Fine-Grained Phase Management for Speculative Decoding in Dynamic LLM Serving

**Authors:** Zhenyu Zhang et al.
**Affiliations:** UC Berkeley, ByteDance
**Source:** [arXiv](https://arxiv.org/abs/2604.20503)
**Date:** 2026-04-22

## Summary
Speculative decoding is the standard for fast LLM inference, but dynamic batching makes it inefficient. FASER introduces phase-aware resource allocation for the draft and target models, vastly improving throughput in production-like serving environments.

## Implementation Notes
Implemented a mock scheduler demonstrating the FASER pipeline phase management logic for draft/target models.
