"""Token-importance weighted on-policy distillation (toy implementation).

The experiment compares uniform token updates against TIP-style token weighting
on a compact sequence generation task: predicting the 2-digit sum of (a, b).
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Dict, List, Sequence, Tuple


VOCAB = list("0123456789")
V = len(VOCAB)
POSITIONS = 2
NUM_PROMPTS = 100  # all (a,b) with a,b in [0,9]


def softmax(logits: Sequence[float]) -> List[float]:
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    s = sum(exps)
    return [e / s for e in exps]


def prompt_id(a: int, b: int) -> int:
    return a * 10 + b


def target_tokens(a: int, b: int) -> List[int]:
    s = f"{a + b:02d}"
    return [ord(s[0]) - ord("0"), ord(s[1]) - ord("0")]


def teacher_distribution(correct_token: int) -> List[float]:
    """Handcrafted teacher distribution with confidence + nearby ambiguity.

    We model a realistic teacher behavior: high confidence on the correct token,
    modest mass on nearby alternatives, tiny mass elsewhere.
    """
    probs = [0.005 for _ in range(V)]
    probs[correct_token] = 0.82
    for neighbor in (correct_token - 1, correct_token + 1):
        if 0 <= neighbor < V:
            probs[neighbor] += 0.08

    # Normalize in case neighbor additions changed total mass.
    s = sum(probs)
    return [p / s for p in probs]


@dataclass
class StudentPolicy:
    """Tabular student policy with one categorical distribution per prompt/position."""

    logits: List[List[List[float]]]

    @staticmethod
    def init(rng: random.Random) -> "StudentPolicy":
        table: List[List[List[float]]] = []
        for _ in range(NUM_PROMPTS):
            row: List[List[float]] = []
            for _ in range(POSITIONS):
                row.append([(rng.random() - 0.5) * 0.04 for _ in range(V)])
            table.append(row)
        return StudentPolicy(logits=table)

    def sample(self, pid: int, rng: random.Random) -> Tuple[List[int], List[List[float]]]:
        sampled: List[int] = []
        probs_by_pos: List[List[float]] = []
        for pos in range(POSITIONS):
            probs = softmax(self.logits[pid][pos])
            r = rng.random()
            c = 0.0
            tok = V - 1
            for i, p in enumerate(probs):
                c += p
                if r <= c:
                    tok = i
                    break
            sampled.append(tok)
            probs_by_pos.append(probs)
        return sampled, probs_by_pos

    def greedy(self, pid: int) -> List[int]:
        return [
            max(range(V), key=lambda t: softmax(self.logits[pid][pos])[t])
            for pos in range(POSITIONS)
        ]


def token_importance(sampled_tok: int, teacher_probs: List[float]) -> float:
    """TIP-style weight: prioritize tokens where teacher disagrees with student.

    If the student sampled a token the teacher finds unlikely, this update should
    matter more. We add a floor term to avoid zeroing any token entirely.
    """
    return 0.05 + (1.0 - teacher_probs[sampled_tok])


def train(mode: str, seed: int = 7, steps: int = 14000) -> Dict[str, float]:
    rng = random.Random(seed)
    student = StudentPolicy.init(rng)

    lr = 0.09
    importance_accumulator = 0.0

    for _ in range(steps):
        a = rng.randint(0, 9)
        b = rng.randint(0, 9)
        pid = prompt_id(a, b)

        sampled, student_probs = student.sample(pid, rng)
        target = target_tokens(a, b)

        for pos in range(POSITIONS):
            teacher_probs = teacher_distribution(target[pos])

            if mode == "uniform":
                w = 1.0
            elif mode == "tip":
                w = token_importance(sampled[pos], teacher_probs)
            else:
                raise ValueError(f"unknown mode: {mode}")

            importance_accumulator += w

            # Distillation gradient for CE(teacher || student):
            # dL/dlogits = student_probs - teacher_probs.
            for tok in range(V):
                grad = student_probs[pos][tok] - teacher_probs[tok]
                student.logits[pid][pos][tok] -= lr * w * grad

    # Evaluation across all prompts.
    exact = 0
    token_hits = 0
    total_tokens = 0
    kl_total = 0.0

    for a in range(10):
        for b in range(10):
            pid = prompt_id(a, b)
            pred = student.greedy(pid)
            tgt = target_tokens(a, b)
            if pred == tgt:
                exact += 1
            token_hits += sum(int(p == t) for p, t in zip(pred, tgt))
            total_tokens += POSITIONS

            # KL(teacher || student) as alignment metric.
            for pos in range(POSITIONS):
                tp = teacher_distribution(tgt[pos])
                sp = softmax(student.logits[pid][pos])
                for tprob, sprob in zip(tp, sp):
                    kl_total += tprob * math.log(max(tprob, 1e-12) / max(sprob, 1e-12))

    return {
        "mode": mode,
        "steps": float(steps),
        "exact_accuracy": exact / 100.0,
        "token_accuracy": token_hits / total_tokens,
        "teacher_student_kl": kl_total / (100.0 * POSITIONS),
        "avg_token_importance": importance_accumulator / (steps * POSITIONS),
    }


def run_comparison(seed: int = 7) -> Dict[str, float]:
    uniform = train("uniform", seed=seed)
    tip = train("tip", seed=seed)

    return {
        "uniform_exact_accuracy": uniform["exact_accuracy"],
        "tip_exact_accuracy": tip["exact_accuracy"],
        "uniform_token_accuracy": uniform["token_accuracy"],
        "tip_token_accuracy": tip["token_accuracy"],
        "uniform_teacher_student_kl": uniform["teacher_student_kl"],
        "tip_teacher_student_kl": tip["teacher_student_kl"],
        "uniform_avg_token_importance": uniform["avg_token_importance"],
        "tip_avg_token_importance": tip["avg_token_importance"],
    }
