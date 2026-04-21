#!/usr/bin/env python3
"""Minimal MathNet-style retrieval + RAG demo (multilingual toy data)."""

from __future__ import annotations

from dataclasses import dataclass
from collections import Counter
from math import sqrt
from typing import List, Dict, Tuple


@dataclass
class Item:
    qid: str
    language: str
    prompt: str
    answer: str
    canonical_group: str


CORPUS = [
    Item("en-1", "en", "What is 2x + 3 = 11?", "4", "linear_eq_2x_plus_3"),
    Item("es-1", "es", "Resuelve 2x + 3 = 11", "4", "linear_eq_2x_plus_3"),
    Item("fr-1", "fr", "Résoudre 2x + 3 = 11", "4", "linear_eq_2x_plus_3"),
    Item("en-2", "en", "Compute derivative of x^2", "2x", "derivative_x2"),
    Item("ar-1", "ar", "أوجد مشتقة x^2", "2x", "derivative_x2"),
    Item("en-3", "en", "Find area of rectangle 3 by 5", "15", "rect_area_3_5"),
    Item("zh-1", "zh", "求长方形长3宽5的面积", "15", "rect_area_3_5"),
]

QUERIES = [
    Item("q1", "en", "solve equation 2x+3=11", "4", "linear_eq_2x_plus_3"),
    Item("q2", "en", "d/dx of x squared", "2x", "derivative_x2"),
    Item("q3", "en", "rectangle with sides 3 and 5 area", "15", "rect_area_3_5"),
]


def trigrams(s: str) -> Counter:
    s = " " + s.lower().strip() + " "
    grams = [s[i:i+3] for i in range(max(1, len(s)-2))]
    return Counter(grams)


def cosine(a: Counter, b: Counter) -> float:
    dot = sum(v * b.get(k, 0) for k, v in a.items())
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def retrieve(query: str, k: int = 3) -> List[Tuple[Item, float]]:
    qv = trigrams(query)
    scored = [(it, cosine(qv, trigrams(it.prompt))) for it in CORPUS]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]


def evaluate_recall_at_k(k: int = 3) -> float:
    hit = 0
    for q in QUERIES:
        top = retrieve(q.prompt, k=k)
        groups = [it.canonical_group for it, _ in top]
        ok = q.canonical_group in groups
        hit += int(ok)
        print(f"{q.qid}: groups@{k}={groups} hit={ok}")
    return hit / len(QUERIES)


def rag_solve(query: Item, k: int = 2) -> str:
    ctx = retrieve(query.prompt, k=k)
    # Simple heuristic: vote by canonical group, then copy answer from top item in winning group
    vote: Dict[str, int] = {}
    for it, _ in ctx:
        vote[it.canonical_group] = vote.get(it.canonical_group, 0) + 1
    best_group = max(vote, key=vote.get)
    for it, _ in ctx:
        if it.canonical_group == best_group:
            return it.answer
    return ""


def evaluate_rag() -> float:
    correct = 0
    for q in QUERIES:
        pred = rag_solve(q, k=2)
        ok = pred == q.answer
        correct += int(ok)
        print(f"RAG {q.qid}: pred={pred} gold={q.answer} ok={ok}")
    return correct / len(QUERIES)


def main() -> None:
    print("=== Retrieval evaluation ===")
    r3 = evaluate_recall_at_k(3)
    print(f"Recall@3 = {r3:.2%}\n")

    print("=== Retrieval-augmented solving ===")
    acc = evaluate_rag()
    print(f"RAG accuracy = {acc:.2%}")


if __name__ == "__main__":
    main()
