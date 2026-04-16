"""Toy simulator for low-depth distributed quantum search."""

from __future__ import annotations

import cmath
import math
import random
from typing import Dict, List


def uniform_state(n: int) -> List[complex]:
    """Return uniform superposition over n basis states."""
    amp = 1.0 / math.sqrt(n)
    return [complex(amp, 0.0) for _ in range(n)]


def apply_oracle(state: List[complex], marked_index: int) -> None:
    """Phase oracle for one marked element: |m> -> -|m>."""
    state[marked_index] *= -1


def apply_diffusion(state: List[complex]) -> None:
    """Inversion-about-mean diffusion operator.

    This is the core Grover amplitude amplification step after the oracle.
    """
    mean_amp = sum(state) / len(state)
    for i, amp in enumerate(state):
        state[i] = 2 * mean_amp - amp


def grover_state(n: int, marked_index: int, iterations: int) -> List[complex]:
    """Compute final state after a chosen number of Grover iterations."""
    state = uniform_state(n)
    for _ in range(iterations):
        apply_oracle(state, marked_index)
        apply_diffusion(state)
    return state


def sample_index(probabilities: List[float], rng: random.Random) -> int:
    r = rng.random()
    c = 0.0
    for i, p in enumerate(probabilities):
        c += p
        if r <= c:
            return i
    return len(probabilities) - 1


def success_probability_from_state(state: List[complex], marked_index: int) -> float:
    return abs(state[marked_index]) ** 2


def monte_carlo_success(state: List[complex], marked_index: int, trials: int, rng: random.Random) -> float:
    probs = [abs(a) ** 2 for a in state]
    hits = 0
    for _ in range(trials):
        obs = sample_index(probs, rng)
        if obs == marked_index:
            hits += 1
    return hits / trials


def recommended_iterations(n: int) -> int:
    return max(1, round((math.pi / 4.0) * math.sqrt(n)))


def depth_proxy(n_states: int, iterations: int) -> float:
    """Simple depth proxy used for relative comparison.

    We approximate each Grover iteration cost as proportional to qubit count.
    This is not hardware-accurate, but useful for illustrating depth scaling.
    """
    qubits = int(round(math.log2(n_states)))
    return float(iterations * 2 * qubits)


def run_demo(seed: int = 23) -> Dict[str, float]:
    rng = random.Random(seed)

    n = 64
    marked = 41
    shards = 4
    shard_size = n // shards

    # Centralized Grover over all items.
    central_iters = recommended_iterations(n)
    central_state = grover_state(n, marked, central_iters)
    central_success_theory = success_probability_from_state(central_state, marked)
    central_success_mc = monte_carlo_success(central_state, marked, trials=4000, rng=rng)
    central_depth = depth_proxy(n, central_iters)

    # Distributed mode: all shards run in parallel, each over shard_size items.
    marked_shard = marked // shard_size
    local_marked_index = marked % shard_size
    local_iters = recommended_iterations(shard_size)

    # Success depends on marked shard producing the correct index.
    marked_shard_state = grover_state(shard_size, local_marked_index, local_iters)
    distributed_success_theory = success_probability_from_state(marked_shard_state, local_marked_index)
    distributed_success_mc = monte_carlo_success(marked_shard_state, local_marked_index, trials=4000, rng=rng)

    # Parallel wall-clock depth roughly equals local depth + tiny verification overhead.
    distributed_depth = depth_proxy(shard_size, local_iters) + 1.0

    return {
        "database_size": float(n),
        "shards": float(shards),
        "central_iterations": float(central_iters),
        "distributed_local_iterations": float(local_iters),
        "central_success_theory": central_success_theory,
        "distributed_success_theory": distributed_success_theory,
        "central_success_monte_carlo": central_success_mc,
        "distributed_success_monte_carlo": distributed_success_mc,
        "central_depth_proxy": central_depth,
        "distributed_depth_proxy": distributed_depth,
        "depth_reduction_ratio": 1.0 - (distributed_depth / central_depth),
    }
