#!/usr/bin/env python3
"""FASTER-style value-guided candidate pruning simulation."""
import random
import statistics


def run_episode(rnd, n_candidates=16, denoise_steps=8, keep_ratio=0.5):
    # latent true action quality
    qualities = [rnd.gauss(0, 1) for _ in range(n_candidates)]

    # Baseline compute: evaluate all candidates through all steps
    baseline_compute = n_candidates * denoise_steps
    baseline_return = max(qualities)

    # FASTER-like: early estimate + pruning
    active = list(range(n_candidates))
    compute = 0
    for step in range(denoise_steps):
        # value estimate improves with step
        est_noise = max(0.15, 0.8 - 0.08 * step)
        scores = []
        for i in active:
            pred = qualities[i] + rnd.gauss(0, est_noise)
            scores.append((pred, i))
            compute += 1

        # prune at mid-steps
        if step in (1, 3, 5) and len(active) > 2:
            scores.sort(reverse=True)
            k = max(2, int(len(active) * keep_ratio))
            active = [i for _, i in scores[:k]]

    faster_return = max(qualities[i] for i in active)
    return baseline_return, faster_return, baseline_compute, compute


if __name__ == "__main__":
    rnd = random.Random(123)
    episodes = 300
    base_ret, fast_ret, base_c, fast_c = [], [], [], []

    for _ in range(episodes):
        b, f, bc, fc = run_episode(rnd)
        base_ret.append(b)
        fast_ret.append(f)
        base_c.append(bc)
        fast_c.append(fc)

    regret = statistics.mean(b - f for b, f in zip(base_ret, fast_ret))
    speedup = statistics.mean(bc / fc for bc, fc in zip(base_c, fast_c))

    print(f"Baseline avg return: {statistics.mean(base_ret):.4f}")
    print(f"FASTER-like avg return: {statistics.mean(fast_ret):.4f}")
    print(f"Average regret vs full sampling: {regret:.4f}")
    print(f"Average compute speedup: {speedup:.2f}x")
