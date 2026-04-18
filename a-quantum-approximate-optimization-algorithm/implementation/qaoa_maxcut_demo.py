#!/usr/bin/env python3
"""Minimal p=1 QAOA simulator for MaxCut on a 3-node triangle graph."""

import cmath
import math

N_QUBITS = 3
DIM = 1 << N_QUBITS
EDGES = [(0, 1), (1, 2), (0, 2)]


def bit(z, q):
    return (z >> q) & 1


def cut_value(z):
    return sum(1 for i, j in EDGES if bit(z, i) ^ bit(z, j))


def init_uniform_state():
    amp = 1 / math.sqrt(DIM)
    return [complex(amp, 0.0) for _ in range(DIM)]


def apply_cost_phase(state, gamma):
    out = state[:]
    for z in range(DIM):
        phase = cmath.exp(-1j * gamma * cut_value(z))
        out[z] *= phase
    return out


def apply_rx_single(state, qubit, beta):
    c = math.cos(beta)
    s = -1j * math.sin(beta)
    out = state[:]
    for z in range(DIM):
        if bit(z, qubit) == 0:
            z0 = z
            z1 = z | (1 << qubit)
            a0 = state[z0]
            a1 = state[z1]
            out[z0] = c * a0 + s * a1
            out[z1] = s * a0 + c * a1
    return out


def apply_mixer(state, beta):
    out = state[:]
    for q in range(N_QUBITS):
        out = apply_rx_single(out, q, beta)
    return out


def expected_cut(state):
    exp = 0.0
    probs = []
    for z, amp in enumerate(state):
        p = (amp.real * amp.real + amp.imag * amp.imag)
        probs.append((z, p))
        exp += p * cut_value(z)
    probs.sort(key=lambda x: x[1], reverse=True)
    return exp, probs


def format_bits(z):
    return format(z, f'0{N_QUBITS}b')


def main():
    best = None
    for i in range(31):
        gamma = math.pi * i / 30.0
        for j in range(31):
            beta = (math.pi / 2) * j / 30.0
            state = init_uniform_state()
            state = apply_cost_phase(state, gamma)
            state = apply_mixer(state, beta)
            exp_cut, probs = expected_cut(state)
            if best is None or exp_cut > best[0]:
                best = (exp_cut, gamma, beta, probs)

    exp_cut, gamma, beta, probs = best
    print('=== QAOA p=1 MaxCut demo (triangle graph) ===')
    print(f'Best expected cut: {exp_cut:.4f} (max possible is 2.0 on triangle)')
    print(f'Best gamma: {gamma:.4f}, best beta: {beta:.4f}')
    print('Top bitstrings by probability:')
    for z, p in probs[:6]:
        print(f'  {format_bits(z)} -> p={p:.4f}, cut={cut_value(z)}')


if __name__ == '__main__':
    main()
