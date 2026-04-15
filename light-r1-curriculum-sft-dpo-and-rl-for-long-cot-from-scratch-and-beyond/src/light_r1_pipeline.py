"""Toy Light-R1 pipeline: curriculum SFT -> DPO -> GRPO.

The goal is to make the training recipe executable and inspectable without requiring
a full LLM stack. We model a policy that chooses one of two reasoning strategies:

- direct: answer quickly, good on easy tasks, brittle on hard tasks
- decompose: chain-of-thought style decomposition, better on hard tasks

A single logistic policy decides which strategy to use based on task difficulty.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Dict, List, Tuple


def sigmoid(x: float) -> float:
    # Numerically stable sigmoid for optimization loops.
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


@dataclass
class StrategyPolicy:
    """Binary policy over {direct, decompose} parameterized by difficulty.

    p(decompose | d) = sigmoid(theta0 + theta1 * d)
    """

    theta0: float = -1.0
    theta1: float = 2.0

    def prob_decompose(self, difficulty: float) -> float:
        return sigmoid(self.theta0 + self.theta1 * difficulty)

    def sample_action(self, difficulty: float, rng: random.Random) -> int:
        # action=1 means decompose, action=0 means direct.
        return 1 if rng.random() < self.prob_decompose(difficulty) else 0

    def grad_logprob(self, difficulty: float, action: int) -> Tuple[float, float]:
        # Gradient of log pi(a|d) wrt theta0/theta1.
        p = self.prob_decompose(difficulty)
        coeff = (action - p)
        return coeff, coeff * difficulty

    def update(self, g0: float, g1: float, lr: float) -> None:
        self.theta0 += lr * g0
        self.theta1 += lr * g1


def oracle_action(difficulty: float) -> int:
    """Teacher preference for reasoning strategy.

    Easier tasks are usually solved directly; harder tasks benefit from decomposition.
    """
    return 1 if difficulty >= 0.45 else 0


def reward_model(difficulty: float, action: int, rng: random.Random) -> float:
    """Environment reward proxy for task success.

    This simulates that decomposition scales better with difficulty while direct
    reasoning degrades on hard examples.
    """
    if action == 1:  # decompose
        success_prob = min(0.98, 0.78 + 0.20 * difficulty)
    else:  # direct
        success_prob = max(0.05, 0.93 - 0.60 * difficulty)
    return 1.0 if rng.random() < success_prob else 0.0


def evaluate(policy: StrategyPolicy, rng: random.Random, n: int = 2500) -> float:
    """Monte-Carlo estimate of end-task accuracy."""
    hits = 0
    for _ in range(n):
        d = rng.random()
        a = 1 if rng.random() < policy.prob_decompose(d) else 0
        hits += int(reward_model(d, a, rng) > 0.5)
    return hits / n


def curriculum_sft(policy: StrategyPolicy, rng: random.Random) -> None:
    """Stage 1: curriculum supervised fine-tuning.

    We train across increasing difficulty bands so the policy first internalizes easy
    behavior, then gradually learns robust strategy switching for harder tasks.
    """
    bands = [(0.00, 0.25), (0.25, 0.50), (0.50, 0.75), (0.75, 1.00)]
    for lo, hi in bands:
        for _ in range(300):
            d = lo + (hi - lo) * rng.random()
            y = oracle_action(d)
            p = policy.prob_decompose(d)
            # BCE gradient for logistic classifier.
            g0 = (y - p)
            g1 = (y - p) * d
            policy.update(g0, g1, lr=0.10)


def dpo_stage(policy: StrategyPolicy, rng: random.Random) -> None:
    """Stage 2: DPO-style preference optimization.

    For each prompt, we compare preferred vs rejected reasoning styles and optimize
    log-sigmoid(beta * (log pi(chosen) - log pi(rejected))).
    """
    beta = 1.8
    for _ in range(1000):
        d = rng.random()
        chosen = oracle_action(d)
        rejected = 1 - chosen
        p = policy.prob_decompose(d)
        # log pi(action) for binary policy
        logp_chosen = math.log(max(1e-8, p if chosen == 1 else 1 - p))
        logp_rejected = math.log(max(1e-8, p if rejected == 1 else 1 - p))
        margin = beta * (logp_chosen - logp_rejected)
        # derivative of log(sigmoid(margin)) wrt margin is 1-sigmoid(margin)
        scale = (1.0 - sigmoid(margin)) * beta

        g0_c, g1_c = policy.grad_logprob(d, chosen)
        g0_r, g1_r = policy.grad_logprob(d, rejected)
        g0 = scale * (g0_c - g0_r)
        g1 = scale * (g1_c - g1_r)
        policy.update(g0, g1, lr=0.04)


def grpo_stage(policy: StrategyPolicy, rng: random.Random) -> None:
    """Stage 3: group-relative policy optimization (GRPO-style).

    For each prompt we sample a group of trajectories, normalize rewards by group
    mean/std, and apply policy-gradient updates with relative advantages.
    """
    group_size = 6
    for _ in range(600):
        d = rng.random()
        samples: List[Tuple[int, float]] = []
        for _ in range(group_size):
            a = policy.sample_action(d, rng)
            r = reward_model(d, a, rng)
            samples.append((a, r))

        rewards = [r for _, r in samples]
        mean_r = sum(rewards) / len(rewards)
        var_r = sum((r - mean_r) ** 2 for r in rewards) / len(rewards)
        std_r = math.sqrt(var_r + 1e-6)

        g0 = 0.0
        g1 = 0.0
        for a, r in samples:
            adv = (r - mean_r) / std_r
            dg0, dg1 = policy.grad_logprob(d, a)
            g0 += adv * dg0
            g1 += adv * dg1

        g0 /= group_size
        g1 /= group_size
        policy.update(g0, g1, lr=0.03)


def run_demo(seed: int = 7) -> Dict[str, float]:
    rng = random.Random(seed)
    policy = StrategyPolicy()

    baseline = evaluate(policy, rng)
    curriculum_sft(policy, rng)
    after_sft = evaluate(policy, rng)
    dpo_stage(policy, rng)
    after_dpo = evaluate(policy, rng)
    grpo_stage(policy, rng)
    after_grpo = evaluate(policy, rng)

    return {
        "baseline_accuracy": baseline,
        "after_curriculum_sft": after_sft,
        "after_dpo": after_dpo,
        "after_grpo": after_grpo,
        "theta0": policy.theta0,
        "theta1": policy.theta1,
    }


if __name__ == "__main__":
    metrics = run_demo()
    print("Light-R1 toy pipeline metrics:")
    for k, v in metrics.items():
        if isinstance(v, float):
            print(f"- {k}: {v:.4f}")
        else:
            print(f"- {k}: {v}")
