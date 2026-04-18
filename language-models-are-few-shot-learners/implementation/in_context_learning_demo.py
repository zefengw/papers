#!/usr/bin/env python3
"""Toy in-context learning demo: classify texts with few-shot support examples.

No model weights are updated. Prediction is performed only from provided examples,
mirroring the paper's key operational idea of few-shot prompting without fine-tuning.
"""

import math
import re
from collections import Counter, defaultdict


def tokenize(text):
    return re.findall(r"[a-zA-Z']+", text.lower())


def vectorize(tokens):
    return Counter(tokens)


def cosine_sim(a, b):
    common = set(a) & set(b)
    dot = sum(a[t] * b[t] for t in common)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def classify(query, support):
    qv = vectorize(tokenize(query))
    scores = defaultdict(float)
    for text, label in support:
        sv = vectorize(tokenize(text))
        scores[label] += max(0.0, cosine_sim(qv, sv))
    return max(scores.items(), key=lambda kv: kv[1])[0], dict(scores)


def main():
    support = [
        ("The product works perfectly and I love it", "positive"),
        ("Excellent service and very fast delivery", "positive"),
        ("This is broken and very disappointing", "negative"),
        ("Terrible quality and poor customer support", "negative"),
    ]

    queries = [
        "Fast shipping and excellent quality",
        "The item arrived broken and support was terrible",
        "I love this purchase",
        "Very disappointing experience",
    ]

    print("=== Few-shot sentiment classification (no training updates) ===")
    for q in queries:
        pred, raw = classify(q, support)
        print(f"\nQuery: {q}")
        print(f"Predicted label: {pred}")
        print(f"Label scores: { {k: round(v, 4) for k, v in raw.items()} }")


if __name__ == "__main__":
    main()
