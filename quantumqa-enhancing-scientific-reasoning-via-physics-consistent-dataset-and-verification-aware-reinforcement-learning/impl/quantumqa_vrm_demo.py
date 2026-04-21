#!/usr/bin/env python3
"""QuantumQA-style verification-aware reward demo."""

from __future__ import annotations

import cmath
import random
from dataclasses import dataclass
from typing import List


@dataclass
class Candidate:
    text: str
    amplitudes: List[complex]  # toy wavefunction


def deterministic_physics_score(amps: List[complex]) -> float:
    probs = [abs(a) ** 2 for a in amps]
    norm = sum(probs)
    if any(p < -1e-9 or p > 1 + 1e-9 for p in probs):
        return 0.0
    # normalization closeness
    return max(0.0, 1.0 - abs(norm - 1.0))


def semantic_score(text: str) -> float:
    t = text.lower()
    score = 0.2
    if "normalization" in t:
        score += 0.25
    if "probability" in t:
        score += 0.2
    if "measurement" in t:
        score += 0.2
    if "because" in t or "therefore" in t:
        score += 0.15
    return min(score, 1.0)


def adaptive_reward_fusion(det: float, sem: float) -> float:
    # Emphasize deterministic signal when violation risk is high.
    alpha = 0.75 if det < 0.7 else 0.55
    return alpha * det + (1 - alpha) * sem


def pick_best(cands: List[Candidate]) -> Candidate:
    scored = []
    for c in cands:
        det = deterministic_physics_score(c.amplitudes)
        sem = semantic_score(c.text)
        rew = adaptive_reward_fusion(det, sem)
        scored.append((rew, det, sem, c))
    scored.sort(key=lambda x: x[0], reverse=True)
    for rew, det, sem, c in scored:
        print(f"reward={rew:.3f} det={det:.3f} sem={sem:.3f} :: {c.text[:80]}")
    return scored[0][3]


def main() -> None:
    random.seed(7)
    cands = [
        Candidate(
            text="The state is valid because normalization holds and measurement probability sums to 1.",
            amplitudes=[0.8 + 0j, 0.6 + 0j],
        ),
        Candidate(
            text="Probability seems okay but I ignore normalization details.",
            amplitudes=[1.0 + 0j, 1.0 + 0j],
        ),
        Candidate(
            text="Therefore measurement outcomes follow Born probability after normalization.",
            amplitudes=[1 / cmath.sqrt(2), 1 / cmath.sqrt(2)],
        ),
    ]

    print("=== Candidate ranking with verification-aware reward ===")
    best = pick_best(cands)
    print("\nSelected best candidate:")
    print(best.text)


if __name__ == "__main__":
    main()
