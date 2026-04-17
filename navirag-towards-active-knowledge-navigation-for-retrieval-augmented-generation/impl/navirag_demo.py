#!/usr/bin/env python3
"""Minimal NaviRAG-style hierarchical navigation demo (stdlib only)."""
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Node:
    level: str
    text: str
    children: List[int]


def tokenize(s: str) -> set[str]:
    return {w.strip('.,:;!?()[]{}').lower() for w in s.split() if w.strip()}


def score(query: str, text: str) -> int:
    return len(tokenize(query) & tokenize(text))


def build_knowledge_graph() -> Dict[int, Node]:
    return {
        0: Node('topic', 'RAG systems for long legal documents', [1, 2]),
        1: Node('subtopic', 'Contract clauses: liability, indemnity, termination windows', [3, 4]),
        2: Node('subtopic', 'Compliance clauses: retention, audit, privacy obligations', [5]),
        3: Node('evidence', 'Termination requires 30-day notice except material breach.', []),
        4: Node('evidence', 'Liability cap excludes fraud and confidentiality breaches.', []),
        5: Node('evidence', 'Audit logs must be retained for 7 years.', []),
    }


def navigate(query: str, graph: Dict[int, Node], start: int = 0, max_steps: int = 4) -> List[int]:
    path = [start]
    current = start
    for _ in range(max_steps):
        children = graph[current].children
        if not children:
            break
        current = max(children, key=lambda cid: score(query, graph[cid].text))
        path.append(current)
    return path


def main() -> None:
    query = 'What is the termination notice requirement in the contract?'
    graph = build_knowledge_graph()
    path = navigate(query, graph)

    print('Query:', query)
    print('Navigation path:')
    for pid in path:
        n = graph[pid]
        print(f'- [{n.level}] {n.text}')

    evidence = [graph[i].text for i in path if graph[i].level == 'evidence']
    answer = evidence[0] if evidence else 'No evidence found.'
    print('\nSynthesized answer:')
    print(answer)


if __name__ == '__main__':
    main()
