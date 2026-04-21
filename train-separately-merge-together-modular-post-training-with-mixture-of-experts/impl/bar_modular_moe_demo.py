#!/usr/bin/env python3
"""Toy BAR-style modular MoE post-training demo.

This script demonstrates:
1) Independent experts with domain specialization.
2) Lightweight router selecting experts based on task signal.
3) Easy expert upgrades without retraining all experts.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Example:
    task: str
    prompt: str
    expected_expert: str


EXPERTS = ["general", "math", "code", "tool", "safety"]

# Router keyword priors (logit bonuses).
ROUTER_PRIORS: Dict[str, Dict[str, float]] = {
    "math": {"integral": 3.0, "equation": 2.6, "solve": 1.5, "proof": 2.2},
    "code": {"python": 3.0, "bug": 2.2, "function": 1.8, "compile": 2.0},
    "tool": {"search": 2.5, "browser": 2.4, "api": 2.0, "retrieve": 1.6},
    "safety": {"harm": 2.5, "unsafe": 2.6, "policy": 2.2, "jailbreak": 2.7},
}

BASE_LOGITS = {e: 0.2 for e in EXPERTS}
BASE_LOGITS["general"] = 0.6


def softmax(xs: Dict[str, float]) -> Dict[str, float]:
    m = max(xs.values())
    exps = {k: math.exp(v - m) for k, v in xs.items()}
    z = sum(exps.values())
    return {k: v / z for k, v in exps.items()}


def route(prompt: str) -> Tuple[str, Dict[str, float]]:
    p = prompt.lower()
    logits = dict(BASE_LOGITS)
    for expert, kw in ROUTER_PRIORS.items():
        for token, bonus in kw.items():
            if token in p:
                logits[expert] += bonus
    probs = softmax(logits)
    best = max(probs, key=probs.get)
    return best, probs


def evaluate(examples: List[Example]) -> float:
    correct = 0
    for ex in examples:
        pred, probs = route(ex.prompt)
        ok = pred == ex.expected_expert
        correct += int(ok)
        top2 = sorted(probs.items(), key=lambda kv: kv[1], reverse=True)[:2]
        print(f"[{ex.task}] pred={pred:7s} expected={ex.expected_expert:7s} ok={ok} top2={top2}")
    return correct / len(examples)


def upgrade_math_expert():
    """Simulate cheap domain update: improve math routing only."""
    ROUTER_PRIORS["math"].update({"theorem": 2.8, "derivative": 2.7, "matrix": 2.0})


def main() -> None:
    dev = [
        Example("calc", "solve this integral and show equation steps", "math"),
        Example("coding", "python function has a bug, help compile", "code"),
        Example("agent", "search browser api and retrieve docs", "tool"),
        Example("alignment", "this jailbreak prompt seems unsafe", "safety"),
        Example("general", "summarize this paragraph", "general"),
        Example("algebra", "prove this theorem about matrix derivative", "math"),
    ]

    print("=== Before expert upgrade ===")
    acc1 = evaluate(dev)
    print(f"Router accuracy: {acc1:.2%}\n")

    print("=== Upgrade only math expert/router hooks ===")
    upgrade_math_expert()
    acc2 = evaluate(dev)
    print(f"Router accuracy after targeted update: {acc2:.2%}")


if __name__ == "__main__":
    main()
