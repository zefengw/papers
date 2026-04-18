#!/usr/bin/env python3
"""
UniDetect-inspired toy pipeline:
- Build account-level transaction features from heterogeneous chains
- Generate pseudo "LLM summary" text features
- Alternate updates of graph score and text score to mimic two-stage training
"""

from dataclasses import dataclass
from random import Random
import math


@dataclass
class Account:
    tx_count: int
    avg_value: float
    bridge_ratio: float
    mixer_ratio: float
    summary_risk: float
    label: int


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def make_dataset(n=400, seed=11):
    rng = Random(seed)
    data = []
    for _ in range(n):
        label = 1 if rng.random() < 0.35 else 0
        if label:
            tx = rng.randint(80, 900)
            avg = rng.uniform(3.0, 80.0)
            bridge = rng.uniform(0.35, 0.95)
            mixer = rng.uniform(0.15, 0.9)
            txt = rng.uniform(0.55, 0.98)
        else:
            tx = rng.randint(5, 500)
            avg = rng.uniform(0.02, 20.0)
            bridge = rng.uniform(0.0, 0.45)
            mixer = rng.uniform(0.0, 0.25)
            txt = rng.uniform(0.02, 0.65)
        data.append(Account(tx, avg, bridge, mixer, txt, label))
    return data


def normalize(a: Account):
    return [
        min(a.tx_count / 1000, 1.0),
        min(a.avg_value / 100, 1.0),
        a.bridge_ratio,
        a.mixer_ratio,
        a.summary_risk,
    ]


def train_alternating(data, epochs=25, lr=0.25):
    # weights: graph block (0..3), text block (4)
    w = [0.2, 0.2, 0.3, 0.3, 0.2]
    b = -0.4

    for ep in range(epochs):
        # stage A: graph-centric update
        for acc in data:
            x = normalize(acc)
            z = b + sum(w[i] * x[i] for i in range(4)) + 0.15 * w[4] * x[4]
            p = sigmoid(z)
            e = acc.label - p
            for i in range(4):
                w[i] += lr * e * x[i]
            b += lr * e

        # stage B: text-centric update
        for acc in data:
            x = normalize(acc)
            z = b + 0.25 * sum(w[i] * x[i] for i in range(4)) + w[4] * x[4]
            p = sigmoid(z)
            e = acc.label - p
            w[4] += lr * e * x[4]
            b += 0.4 * lr * e

    return w, b


def evaluate(data, w, b):
    tp = fp = tn = fn = 0
    for acc in data:
        x = normalize(acc)
        p = sigmoid(b + sum(w[i] * x[i] for i in range(5)))
        y = 1 if p >= 0.5 else 0
        if y == 1 and acc.label == 1: tp += 1
        elif y == 1 and acc.label == 0: fp += 1
        elif y == 0 and acc.label == 0: tn += 1
        else: fn += 1
    precision = tp / (tp + fp + 1e-9)
    recall = tp / (tp + fn + 1e-9)
    f1 = 2 * precision * recall / (precision + recall + 1e-9)
    acc = (tp + tn) / (tp + tn + fp + fn)
    return {"precision": precision, "recall": recall, "f1": f1, "accuracy": acc}


def main():
    train = make_dataset(500, seed=21)
    test = make_dataset(250, seed=22)
    w, b = train_alternating(train)
    m = evaluate(test, w, b)

    print("=== UniDetect Two-Stage Demo ===")
    print("weights:", [round(v, 3) for v in w], "bias:", round(b, 3))
    print("metrics:")
    for k, v in m.items():
        print(f"  {k:>9}: {v:.3f}")


if __name__ == "__main__":
    main()
