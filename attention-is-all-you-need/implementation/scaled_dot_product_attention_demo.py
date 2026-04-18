#!/usr/bin/env python3
"""Minimal scaled dot-product attention demo (Transformer core primitive)."""

import math
from pprint import pprint


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def softmax(logits):
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    s = sum(exps)
    return [x / s for x in exps]


def attention(q, k, v, mask=None):
    d = len(q[0])
    scale = 1.0 / math.sqrt(d)

    weights = []
    outputs = []
    for i, qi in enumerate(q):
        logits = [dot(qi, kj) * scale for kj in k]
        if mask is not None:
            logits = [logits[j] + mask[i][j] for j in range(len(logits))]
        w = softmax(logits)
        o = [sum(wj * vj[t] for wj, vj in zip(w, v)) for t in range(len(v[0]))]
        weights.append(w)
        outputs.append(o)
    return weights, outputs


def make_causal_mask(seq_len):
    neg = -1e9
    return [[0.0 if j <= i else neg for j in range(seq_len)] for i in range(seq_len)]


def main():
    q = [
        [0.5, 0.1, 0.0, 0.2],
        [0.2, 0.6, 0.1, 0.0],
        [0.0, 0.1, 0.8, 0.2],
        [0.3, 0.0, 0.2, 0.7],
    ]
    k = [
        [0.6, 0.0, 0.1, 0.2],
        [0.1, 0.7, 0.2, 0.1],
        [0.0, 0.2, 0.9, 0.0],
        [0.3, 0.1, 0.1, 0.8],
    ]
    v = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.5, 0.5, 0.5],
    ]

    full_w, full_out = attention(q, k, v)
    causal_w, causal_out = attention(q, k, v, make_causal_mask(len(q)))

    print("=== Full attention weights ===")
    pprint([[round(x, 4) for x in row] for row in full_w])
    print("\n=== Full attention outputs ===")
    pprint([[round(x, 4) for x in row] for row in full_out])

    print("\n=== Causal attention weights ===")
    pprint([[round(x, 4) for x in row] for row in causal_w])
    print("\n=== Causal attention outputs ===")
    pprint([[round(x, 4) for x in row] for row in causal_out])


if __name__ == "__main__":
    main()
