# Critical Notes

- Planner is a first-order approximation; it does not model communication overlap, optimizer sharding details, or failure recovery.
- Storage model assumes sustained write throughput and no metadata contention.
- Does not include post-training stages (SFT/RLHF/RLVR) which can shift bottlenecks from IO to inference serving.

## Extension Ideas

1. Add topology-aware bandwidth model (intra-node NVLink vs inter-node fabric).
2. Simulate preemption/failure impact on effective token throughput.
3. Integrate with real job traces to calibrate efficiency curve.
