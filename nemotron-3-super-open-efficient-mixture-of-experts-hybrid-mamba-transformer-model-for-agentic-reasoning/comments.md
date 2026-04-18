# Critical Notes

- The repository paper reports full-stack engineering (pretrain + post-train + quantization); this demo only captures **efficiency mechanics** conceptually.
- LatentMoE behavior is represented as sparse-routing math, not a full neural implementation.
- Speculative decoding model is simplified and does not model batch-size/sequence-length latency variance.

## Extension Ideas

1. Add an offline trace-based latency model using real tokenizer lengths and KV-cache reuse curves.
2. Implement a tiny MoE toy network (NumPy/PyTorch) with top-k gating and route balancing losses.
3. Add quantization-aware throughput projections (FP16 vs FP8 vs NVFP4) with memory-bandwidth constraints.
