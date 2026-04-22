#!/usr/bin/env python3
"""Toy dynamic-circuit error suppression via learned interval-wise DD schedules."""
import random

PULSES = ["I", "X", "Y", "XY", "XX"]


def pulse_base_effect(pulse):
    # Lower is better global multiplier
    return {
        "I": 1.00,
        "X": 0.89,
        "Y": 0.88,
        "XY": 0.84,
        "XX": 0.86,
    }[pulse]


def mismatch_penalty(chosen, preferred):
    if chosen == preferred:
        return 0.0
    if {chosen, preferred} <= {"X", "Y", "XX", "XY"}:
        return 0.05
    return 0.12


def evaluate(schedule, interval_noise, preferred_pulses):
    # Hardware-aware infidelity: base effect + interval-specific mismatch penalty
    total = 0.0
    for pulse, base_noise, pref in zip(schedule, interval_noise, preferred_pulses):
        mult = pulse_base_effect(pulse)
        mult += mismatch_penalty(pulse, pref)
        total += base_noise * mult
    return total / len(schedule)


def learn_schedule(interval_noise, preferred_pulses, iters=1200, seed=0):
    rnd = random.Random(seed)
    n = len(interval_noise)
    sched = ["I"] * n
    best = evaluate(sched, interval_noise, preferred_pulses)

    for _ in range(iters):
        i = rnd.randrange(n)
        cand = list(sched)
        cand[i] = rnd.choice(PULSES)
        score = evaluate(cand, interval_noise, preferred_pulses)
        if score < best or rnd.random() < 0.01:
            sched, best = cand, score
    return sched, best


if __name__ == "__main__":
    rnd = random.Random(2026)
    # dynamic-circuit intervals: measurement/control phases are noisier
    interval_noise = [rnd.uniform(0.015, 0.055) for _ in range(20)]
    for i in [4, 9, 14]:
        interval_noise[i] *= 1.8

    # Hidden hardware preference varies by interval/sub-register context
    # (biased away from XY to make fixed-template limitations visible)
    preferred_pulses = [rnd.choice(["X", "Y", "XX", "X", "Y", "XX", "I"]) for _ in interval_noise]

    fixed_schedule = ["XY"] * len(interval_noise)
    fixed_err = evaluate(fixed_schedule, interval_noise, preferred_pulses)

    learned_schedule, learned_err = learn_schedule(interval_noise, preferred_pulses)

    print(f"Fixed template error rate:   {fixed_err:.5f}")
    print(f"Learned schedule error rate: {learned_err:.5f}")
    print(f"Improvement factor:          {fixed_err / learned_err:.2f}x")
    print("Learned schedule:", " ".join(learned_schedule))
