#!/usr/bin/env python3
"""
Toy simulation of Nemotron-style efficiency ingredients:
1) LatentMoE sparse activation (active experts only)
2) Speculative decoding acceptance process
3) Throughput/cost estimator under varying acceptance rates

No external dependencies (stdlib only).
"""

from dataclasses import dataclass
from random import Random
from statistics import mean


@dataclass
class ModelConfig:
    total_params_b: float = 120.0
    active_params_b: float = 12.0
    experts: int = 32
    top_k: int = 2


def latent_moe_compute_fraction(cfg: ModelConfig) -> float:
    """Approximate fraction of FFN expert compute used per token."""
    return cfg.top_k / cfg.experts


def simulate_speculative_decode(
    tokens: int = 1024,
    draft_cost: float = 0.2,
    target_cost: float = 1.0,
    accept_prob: float = 0.72,
    seed: int = 7,
):
    """
    Simulate speculative decoding:
    - Draft proposes token
    - Target verifies; accepted tokens amortize target calls
    Returns normalized compute cost and acceptance stats.
    """
    rng = Random(seed)
    accepted = 0
    cost = 0.0
    for _ in range(tokens):
        cost += draft_cost
        if rng.random() < accept_prob:
            accepted += 1
            cost += 0.2 * target_cost  # cheaper verification path
        else:
            cost += target_cost        # full target forward
    baseline = tokens * target_cost
    speedup = baseline / cost
    return {
        "tokens": tokens,
        "accepted": accepted,
        "accept_rate": accepted / tokens,
        "normalized_cost": cost / baseline,
        "estimated_speedup": speedup,
    }


def run_grid():
    cfg = ModelConfig()
    print("=== Nemotron-style Efficiency Demo ===")
    print(f"Total params (B): {cfg.total_params_b}")
    print(f"Active params (B): {cfg.active_params_b}")
    print(f"Experts: {cfg.experts}, Top-k routing: {cfg.top_k}")
    print(f"Approx MoE FFN compute fraction: {latent_moe_compute_fraction(cfg):.3f}")
    print()

    rates = [0.5, 0.6, 0.7, 0.8, 0.9]
    results = []
    for p in rates:
        trial = simulate_speculative_decode(accept_prob=p)
        results.append(trial)
        print(
            f"accept={p:.1f} -> observed={trial['accept_rate']:.3f}, "
            f"cost={trial['normalized_cost']:.3f}x baseline, "
            f"speedup={trial['estimated_speedup']:.2f}x"
        )

    print("\nAverage speedup across grid:", f"{mean(r['estimated_speedup'] for r in results):.2f}x")


if __name__ == "__main__":
    run_grid()
