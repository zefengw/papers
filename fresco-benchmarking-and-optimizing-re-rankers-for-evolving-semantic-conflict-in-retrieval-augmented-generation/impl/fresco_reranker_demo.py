#!/usr/bin/env python3
"""Minimal FRESCO-style reranking demo (semantic score + recency tradeoff)."""
from dataclasses import dataclass
from datetime import date


@dataclass
class Candidate:
    doc_id: str
    semantic_score: float
    doc_date: date
    text: str


def days_old(d: date, now: date) -> int:
    return max(0, (now - d).days)


def recency_score(d: date, now: date) -> float:
    # Newer docs closer to 1.0
    return 1.0 / (1.0 + days_old(d, now) / 365.0)


def rank(cands, now, w_sem=1.0, w_rec=0.0):
    scored = []
    for c in cands:
        s = w_sem * c.semantic_score + w_rec * recency_score(c.doc_date, now)
        scored.append((s, c))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored


def main() -> None:
    now = date(2026, 4, 17)
    candidates = [
        Candidate('old-rich', 0.95, date(2021, 5, 1), 'High semantic match but outdated fact.'),
        Candidate('fresh-correct', 0.82, date(2026, 3, 28), 'Slightly lower semantic overlap but current fact.'),
        Candidate('fresh-noisy', 0.60, date(2026, 4, 10), 'Recent but weakly relevant.'),
    ]

    sem_only = rank(candidates, now, w_sem=1.0, w_rec=0.0)
    recency_aware = rank(candidates, now, w_sem=0.85, w_rec=0.35)

    print('Semantic-only top:', sem_only[0][1].doc_id)
    print('Recency-aware top:', recency_aware[0][1].doc_id)
    print('\nDetailed recency-aware ranking:')
    for s, c in recency_aware:
        print(f'- {c.doc_id:12s} score={s:.3f} sem={c.semantic_score:.2f} rec={recency_score(c.doc_date, now):.2f}')


if __name__ == '__main__':
    main()
