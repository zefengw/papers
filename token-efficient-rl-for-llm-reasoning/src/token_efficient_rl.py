"""Token-efficient RL toy benchmark.

This script compares two policy-gradient training strategies on a sequence prediction task:
1) Full-token updates (all generated tokens)
2) Selective-token updates (first mismatch onward)

The task is intentionally lightweight and fully runnable without external dependencies.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Dict, List, Sequence, Tuple


VOCAB = list("0123456789")
V = len(VOCAB)
POSITIONS = 2  # two-digit output for sum(a,b) where a,b in [0,9]
NUM_STATES = 100  # all (a,b) pairs


def softmax(logits: Sequence[float]) -> List[float]:
    m = max(logits)
    exps = [math.exp(x - m) for x in logits]
    s = sum(exps)
    return [e / s for e in exps]


def state_id(a: int, b: int) -> int:
    return a * 10 + b


def target_tokens(a: int, b: int) -> List[int]:
    s = f"{a + b:02d}"
    return [ord(s[0]) - ord('0'), ord(s[1]) - ord('0')]


@dataclass
class TabularSequencePolicy:
    """Per-state, per-position categorical policy over digits."""

    # logits[state][position][token]
    logits: List[List[List[float]]]

    @staticmethod
    def init(rng: random.Random) -> "TabularSequencePolicy":
        table = []
        for _ in range(NUM_STATES):
            row = []
            for _ in range(POSITIONS):
                row.append([(rng.random() - 0.5) * 0.02 for _ in range(V)])
            table.append(row)
        return TabularSequencePolicy(logits=table)

    def sample_sequence(self, sid: int, rng: random.Random) -> Tuple[List[int], List[List[float]]]:
        sampled = []
        probs_by_pos = []
        for pos in range(POSITIONS):
            probs = softmax(self.logits[sid][pos])
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

    def greedy_sequence(self, sid: int) -> List[int]:
        out = []
        for pos in range(POSITIONS):
            probs = softmax(self.logits[sid][pos])
            out.append(max(range(V), key=lambda t: probs[t]))
        return out

    def reinforce_update(
        self,
        sid: int,
        sampled: List[int],
        probs_by_pos: List[List[float]],
        advantage: float,
        positions_to_update: List[int],
        lr: float,
    ) -> int:
        """Apply REINFORCE score-function gradient for selected positions."""
        for pos in positions_to_update:
            a = sampled[pos]
            probs = probs_by_pos[pos]
            for tok in range(V):
                grad = (1.0 if tok == a else 0.0) - probs[tok]
                self.logits[sid][pos][tok] += lr * advantage * grad
        return len(positions_to_update)


def informative_positions(pred: List[int], target: List[int]) -> List[int]:
    """Prefix-aware selection: update from first mismatch onward."""
    for i in range(POSITIONS):
        if pred[i] != target[i]:
            return list(range(i, POSITIONS))
    return list(range(POSITIONS))


def train(method: str, seed: int = 11, steps: int = 12000) -> Dict[str, float]:
    rng = random.Random(seed)
    policy = TabularSequencePolicy.init(rng)
    baseline = 0.0
    token_updates = 0

    for _ in range(steps):
        a = rng.randint(0, 9)
        b = rng.randint(0, 9)
        sid = state_id(a, b)
        target = target_tokens(a, b)

        pred, probs_by_pos = policy.sample_sequence(sid, rng)
        matches = sum(int(p == t) for p, t in zip(pred, target))

        # Dense reward avoids collapse while still preferring exact correctness.
        reward = matches / POSITIONS
        if pred == target:
            reward += 0.5

        baseline = 0.98 * baseline + 0.02 * reward
        advantage = reward - baseline

        if method == "full":
            positions = [0, 1]
            lr = 0.050
        elif method == "selective":
            positions = informative_positions(pred, target)
            lr = 0.065
        else:
            raise ValueError(f"Unknown method: {method}")

        token_updates += policy.reinforce_update(
            sid=sid,
            sampled=pred,
            probs_by_pos=probs_by_pos,
            advantage=advantage,
            positions_to_update=positions,
            lr=lr,
        )

    # Evaluate over full state space for deterministic accuracy.
    exact = 0
    token_hits = 0
    total_tokens = 0
    for a in range(10):
        for b in range(10):
            sid = state_id(a, b)
            pred = policy.greedy_sequence(sid)
            target = target_tokens(a, b)
            if pred == target:
                exact += 1
            token_hits += sum(int(p == t) for p, t in zip(pred, target))
            total_tokens += POSITIONS

    return {
        "method": method,
        "steps": float(steps),
        "exact_accuracy": exact / 100.0,
        "token_accuracy": token_hits / total_tokens,
        "token_updates": float(token_updates),
    }


def run_comparison(seed: int = 11) -> Dict[str, float]:
    full = train("full", seed=seed)
    selective = train("selective", seed=seed)

    return {
        "full_exact_accuracy": full["exact_accuracy"],
        "selective_exact_accuracy": selective["exact_accuracy"],
        "full_token_accuracy": full["token_accuracy"],
        "selective_token_accuracy": selective["token_accuracy"],
        "full_token_updates": full["token_updates"],
        "selective_token_updates": selective["token_updates"],
        "update_reduction_ratio": 1.0 - (selective["token_updates"] / full["token_updates"]),
    }


if __name__ == "__main__":
    out = run_comparison()
    for k, v in out.items():
        print(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}")
