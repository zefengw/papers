#!/usr/bin/env python3
"""Toy EVPO simulation (pure Python, no external deps)."""
import random
import statistics


def explained_variance(returns, values):
    # EV = 1 - Var(R - V) / Var(R)
    vr = statistics.pvariance(returns)
    if vr == 0:
        return 0.0
    residual = [r - v for r, v in zip(returns, values)]
    return 1.0 - (statistics.pvariance(residual) / vr)


def var(xs):
    return statistics.pvariance(xs) if len(xs) > 1 else 0.0


def generate_epoch(batch_size, critic_quality, seed):
    rnd = random.Random(seed)
    # latent states
    states = [rnd.uniform(-1.0, 1.0) for _ in range(batch_size)]
    # returns: signal + noise
    returns = [1.2 * s + rnd.gauss(0, 0.8) for s in states]
    # value predictions become better as quality rises
    values = [critic_quality * 1.2 * s + rnd.gauss(0, 1.0 - 0.8 * critic_quality) for s in states]
    return returns, values


def run_sim(epochs=20, batch_size=256):
    rows = []
    for e in range(1, epochs + 1):
        # critic matures over time with jitter
        quality = min(1.0, max(0.0, 0.08 * e + random.uniform(-0.05, 0.05)))
        returns, values = generate_epoch(batch_size, quality, 1000 + e)

        ev = explained_variance(returns, values)
        baseline_mean = statistics.mean(returns)

        adv_critic = [r - v for r, v in zip(returns, values)]
        adv_mean = [r - baseline_mean for r in returns]

        use_critic = ev > 0.0
        adv_evpo = adv_critic if use_critic else adv_mean

        rows.append({
            "epoch": e,
            "quality": quality,
            "ev": ev,
            "var_critic": var(adv_critic),
            "var_mean": var(adv_mean),
            "var_evpo": var(adv_evpo),
            "gate": "critic" if use_critic else "mean",
        })
    return rows


if __name__ == "__main__":
    rows = run_sim()
    print("epoch	EV	gate	Var(critic)	Var(mean)	Var(EVPO)")
    for r in rows:
        print(f"{r['epoch']:02d}	{r['ev']:+.3f}	{r['gate']:>6}	{r['var_critic']:.4f}		{r['var_mean']:.4f}		{r['var_evpo']:.4f}")

    avg_critic = statistics.mean(r["var_critic"] for r in rows)
    avg_mean = statistics.mean(r["var_mean"] for r in rows)
    avg_evpo = statistics.mean(r["var_evpo"] for r in rows)
    print()
    print("Average advantage variance:")
    print(f"  Critic baseline: {avg_critic:.4f}")
    print(f"  Mean baseline:   {avg_mean:.4f}")
    print(f"  EVPO adaptive:   {avg_evpo:.4f}")
