#!/usr/bin/env python3
"""TEMPO-style test-time training toy simulation."""
import random
import statistics
def simulate(steps=200, recalib_every=10, seed=7):
    rnd = random.Random(seed)

    # two independent policy tracks on the same stream
    policy_no = 0.0
    policy_tp = 0.0

    # critic bias drift (reward-model drift)
    critic_bias_no_recal = 0.0
    critic_bias_tempo = 0.0

    acc_no_recal = []
    acc_tempo = []

    # latent task manifold state
    state = 0.0

    for t in range(1, steps + 1):
        # non-stationary test stream
        state = 0.92 * state + rnd.uniform(-0.6, 0.6)
        target = max(-1.0, min(1.0, 0.7 * state))

        # observed gradient estimates are corrupted by critic drift
        g_no = (target - policy_no) + critic_bias_no_recal + rnd.uniform(-0.08, 0.08)
        g_tp = (target - policy_tp) + critic_bias_tempo + rnd.uniform(-0.08, 0.08)

        policy_no += 0.22 * g_no
        policy_tp += 0.22 * g_tp

        # true success peaks when policy matches target
        p_true_no = max(0.01, min(0.99, 1.0 - abs(policy_no - target)))
        p_true_tp = max(0.01, min(0.99, 1.0 - abs(policy_tp - target)))

        acc_no_recal.append(1 if rnd.random() < p_true_no else 0)
        acc_tempo.append(1 if rnd.random() < p_true_tp else 0)

        # drift accumulation
        critic_bias_no_recal += rnd.uniform(-0.09, 0.09)
        critic_bias_tempo += rnd.uniform(-0.035, 0.035)

        if t % recalib_every == 0:
            # periodic critic recalibration using labeled anchor data
            critic_bias_tempo *= 0.08

    return acc_no_recal, acc_tempo


if __name__ == "__main__":
    no_recal, tempo = simulate()
    win = [int(t > n) for n, t in zip(no_recal, tempo)]
    print("No recalibration accuracy:", round(statistics.mean(no_recal), 4))
    print("TEMPO-like recalibration accuracy:", round(statistics.mean(tempo), 4))
    print("TEMPO better-than-baseline step ratio:", round(statistics.mean(win), 4))
