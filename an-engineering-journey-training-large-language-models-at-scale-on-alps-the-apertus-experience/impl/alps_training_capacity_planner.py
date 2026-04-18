#!/usr/bin/env python3
"""
Capacity planner inspired by Apertus engineering lessons:
- Cluster-level token throughput estimate
- Storage checkpoint pressure
- Strong-scaling efficiency projection
"""

from dataclasses import dataclass


@dataclass
class Cluster:
    nodes: int
    gpus_per_node: int
    tokens_per_gpu_s: float
    scaling_efficiency: float
    checkpoint_gb: float
    checkpoint_interval_min: int
    storage_write_gbps: float


def effective_tokens_per_second(c: Cluster) -> float:
    return c.nodes * c.gpus_per_node * c.tokens_per_gpu_s * c.scaling_efficiency


def daily_tokens(c: Cluster) -> float:
    return effective_tokens_per_second(c) * 86400


def checkpoint_utilization(c: Cluster) -> float:
    """Fraction of checkpoint window consumed by storage writes."""
    seconds_to_write = c.checkpoint_gb / c.storage_write_gbps
    window = c.checkpoint_interval_min * 60
    return seconds_to_write / window


def strong_scaling(base_tokens_s: float, gpu_counts):
    """Simple diminishing-return scaling curve."""
    out = []
    for g in gpu_counts:
        eff = 0.98 - 0.06 * ((g / gpu_counts[0]) ** 0.4 - 1)
        eff = max(0.55, min(0.99, eff))
        out.append((g, base_tokens_s * g * eff, eff))
    return out


def main():
    cluster = Cluster(
        nodes=128,
        gpus_per_node=4,
        tokens_per_gpu_s=1850,
        scaling_efficiency=0.82,
        checkpoint_gb=2400,
        checkpoint_interval_min=30,
        storage_write_gbps=55,
    )

    print("=== Alps-style LLM Training Planner ===")
    tps = effective_tokens_per_second(cluster)
    print(f"Effective throughput: {tps:,.0f} tokens/s")
    print(f"Daily token budget:  {daily_tokens(cluster):,.0f} tokens/day")

    util = checkpoint_utilization(cluster)
    print(f"Checkpoint window utilization: {util*100:.1f}%")
    if util > 0.5:
        print("WARNING: checkpointing likely bottlenecks training wall-clock.")

    print("\nStrong-scaling projection")
    for g, tok, eff in strong_scaling(1800, [128, 256, 512, 1024, 2048]):
        print(f"GPUs={g:4d} | eff={eff:.3f} | tokens/s={tok:,.0f}")


if __name__ == "__main__":
    main()
