"""NDAR-inspired QAOA simulation on MaxCut.

This is a deliberately compact simulator meant to expose the remapping logic:
- A noisy device has a persistent physical attractor bitstring.
- Gauge/remapping mask g changes how that physical attractor maps to logical states.
- NDAR iteratively chooses masks to push attractor-induced samples toward better cuts.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Dict, List, Sequence, Tuple


Edge = Tuple[int, int, float]


def xor_bits(a: Sequence[int], b: Sequence[int]) -> Tuple[int, ...]:
    return tuple((x ^ y) for x, y in zip(a, b))


def random_weighted_graph(n: int, p: float, rng: random.Random) -> List[Edge]:
    edges: List[Edge] = []
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                w = 0.5 + rng.random()  # weights in [0.5, 1.5)
                edges.append((i, j, w))
    return edges


def cut_value(bits: Sequence[int], edges: Sequence[Edge]) -> float:
    val = 0.0
    for i, j, w in edges:
        if bits[i] != bits[j]:
            val += w
    return val


def all_bitstrings(n: int) -> List[Tuple[int, ...]]:
    out = []
    for x in range(1 << n):
        out.append(tuple((x >> k) & 1 for k in range(n)))
    return out


@dataclass
class NoisyQAOASim:
    n: int
    edges: List[Edge]
    attractor_physical: Tuple[int, ...]
    noise_strength: float = 0.65
    beta: float = 3.0

    def __post_init__(self) -> None:
        self.states = all_bitstrings(self.n)
        scores = [cut_value(s, self.edges) for s in self.states]
        max_score = max(scores)
        min_score = min(scores)
        span = max(1e-9, max_score - min_score)

        # Build an idealized p=1-like distribution: higher cut => higher probability.
        logits = [self.beta * ((c - min_score) / span) for c in scores]
        m = max(logits)
        exps = [math.exp(z - m) for z in logits]
        zsum = sum(exps)
        self.ideal_probs = [e / zsum for e in exps]

    def sample_ideal_logical(self, rng: random.Random) -> Tuple[int, ...]:
        r = rng.random()
        c = 0.0
        for s, p in zip(self.states, self.ideal_probs):
            c += p
            if r <= c:
                return s
        return self.states[-1]

    def sample_logical(self, gauge_mask: Tuple[int, ...], shots: int, rng: random.Random) -> List[Tuple[int, ...]]:
        """Sample logical outputs under noisy execution and gauge remapping.

        With probability noise_strength, output is dominated by attractor state.
        Gauge mask remaps how this physical attractor appears in logical space:
            logical_attractor = attractor_physical XOR gauge_mask
        """
        out: List[Tuple[int, ...]] = []
        logical_attractor = xor_bits(self.attractor_physical, gauge_mask)
        for _ in range(shots):
            if rng.random() < self.noise_strength:
                out.append(logical_attractor)
            else:
                out.append(self.sample_ideal_logical(rng))
        return out


def best_state(samples: Sequence[Tuple[int, ...]], edges: Sequence[Edge]) -> Tuple[Tuple[int, ...], float]:
    best = None
    best_val = -1.0
    for s in samples:
        v = cut_value(s, edges)
        if v > best_val:
            best_val = v
            best = s
    assert best is not None
    return best, best_val


def run_ndar_demo(seed: int = 19) -> Dict[str, object]:
    rng = random.Random(seed)
    n = 10
    edges = random_weighted_graph(n=n, p=0.55, rng=rng)

    # Compute true optimum (small n so brute-force is feasible).
    states = all_bitstrings(n)
    optimum = max(cut_value(s, edges) for s in states)

    attractor = tuple(rng.randint(0, 1) for _ in range(n))
    sim = NoisyQAOASim(
        n=n,
        edges=edges,
        attractor_physical=attractor,
        noise_strength=0.70,
        beta=3.2,
    )

    shots = 350

    # Baseline: fixed gauge (all zeros), one run.
    zero_mask = tuple(0 for _ in range(n))
    baseline_samples = sim.sample_logical(zero_mask, shots, rng)
    _, baseline_best = best_state(baseline_samples, edges)

    # NDAR loop: iteratively choose mask so attractor maps to last best state.
    mask = zero_mask
    ndar_best = -1.0
    progress = []
    for it in range(1, 7):
        samples = sim.sample_logical(mask, shots, rng)
        best_s, best_v = best_state(samples, edges)
        ndar_best = max(ndar_best, best_v)
        progress.append({"iteration": it, "best_cut": round(best_v, 4), "best_ratio": round(best_v / optimum, 4)})

        # Key remapping step: align logical attractor with best state found so far.
        # Since logical_attractor = physical_attractor XOR mask,
        # choose mask = physical_attractor XOR target_best_state.
        mask = xor_bits(sim.attractor_physical, best_s)

    return {
        "nodes": n,
        "edges": len(edges),
        "optimum_cut": round(optimum, 4),
        "baseline_best_cut": round(baseline_best, 4),
        "baseline_ratio": round(baseline_best / optimum, 4),
        "ndar_best_cut": round(ndar_best, 4),
        "ndar_ratio": round(ndar_best / optimum, 4),
        "ndar_progress": progress,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_ndar_demo(), indent=2))
