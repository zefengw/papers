#!/usr/bin/env python3
"""BLF-style forecasting prototype with Bayesian belief updates."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Evidence:
    note: str
    llr: float  # log-likelihood ratio contribution


@dataclass
class Question:
    q: str
    prior: float
    evidence: List[Evidence]
    outcome: int  # 0/1 observed later


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def logit(p: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    return math.log(p / (1 - p))


def sequential_update(prior: float, evidence: List[Evidence], noise_scale: float = 0.0) -> float:
    l = logit(prior)
    for e in evidence:
        l += e.llr + random.gauss(0, noise_scale)
    return sigmoid(l)


def aggregate_trials(ps: List[float], prior: float, shrink: float = 0.15) -> float:
    # logit-space averaging + shrinkage toward prior
    mean_logit = sum(logit(p) for p in ps) / len(ps)
    target = (1 - shrink) * mean_logit + shrink * logit(prior)
    return sigmoid(target)


def calibrate(p: float, a: float = 0.95, b: float = -0.02) -> float:
    # simple Platt-like affine transform in logit space
    return sigmoid(a * logit(p) + b)


def brier(preds: List[float], ys: List[int]) -> float:
    return sum((p - y) ** 2 for p, y in zip(preds, ys)) / len(preds)


def main() -> None:
    random.seed(42)
    qs = [
        Question(
            q="Will model X beat baseline on benchmark Y this quarter?",
            prior=0.40,
            evidence=[
                Evidence("new training data released", 0.30),
                Evidence("compute budget cut rumor", -0.15),
                Evidence("promising internal eval", 0.35),
            ],
            outcome=1,
        ),
        Question(
            q="Will protocol Z face critical outage this month?",
            prior=0.25,
            evidence=[
                Evidence("recent minor incidents", 0.25),
                Evidence("audit completed", -0.30),
                Evidence("traffic spike expected", 0.10),
            ],
            outcome=0,
        ),
    ]

    final_preds: List[float] = []
    ys: List[int] = []

    for q in qs:
        trials = [sequential_update(q.prior, q.evidence, noise_scale=0.08) for _ in range(6)]
        agg = aggregate_trials(trials, q.prior, shrink=0.2)
        cal = calibrate(agg)
        final_preds.append(cal)
        ys.append(q.outcome)
        print("---")
        print(q.q)
        print(f"trial mean={sum(trials)/len(trials):.3f}, aggregated={agg:.3f}, calibrated={cal:.3f}, outcome={q.outcome}")

    print("\nBrier score:", round(brier(final_preds, ys), 4))


if __name__ == "__main__":
    main()
