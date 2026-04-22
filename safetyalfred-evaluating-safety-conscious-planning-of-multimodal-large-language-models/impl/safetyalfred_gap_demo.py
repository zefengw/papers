#!/usr/bin/env python3
"""Synthetic SafetyALFRED-style recognition vs mitigation gap analysis."""
import random
import statistics

HAZARDS = [
    "open_flame",
    "wet_floor",
    "sharp_object",
    "toxic_mix",
    "overheating",
    "electrical_risk",
]

MODELS = {
    "vision_only": {"recognition": 0.71, "mitigation": 0.39},
    "vision_plus_metadata": {"recognition": 0.83, "mitigation": 0.51},
    "strong_multimodal": {"recognition": 0.88, "mitigation": 0.58},
}


def evaluate(model_name, n=400, seed=42):
    rnd = random.Random(seed)
    base = MODELS[model_name]

    rec_hits, mit_hits = 0, 0
    per_hazard = {h: {"rec": 0, "mit": 0, "count": 0} for h in HAZARDS}

    for _ in range(n):
        h = rnd.choice(HAZARDS)
        # hazard-specific difficulty jitter
        diff = rnd.uniform(-0.08, 0.08)

        p_rec = min(0.99, max(0.01, base["recognition"] + diff))
        # planning is harder and depends partially on recognition success
        p_mit = min(0.99, max(0.01, base["mitigation"] + 0.35 * (p_rec - 0.5) + diff / 2))

        rec = 1 if rnd.random() < p_rec else 0
        mit = 1 if rnd.random() < p_mit else 0

        rec_hits += rec
        mit_hits += mit
        per_hazard[h]["rec"] += rec
        per_hazard[h]["mit"] += mit
        per_hazard[h]["count"] += 1

    rec_acc = rec_hits / n
    mit_acc = mit_hits / n
    gap = rec_acc - mit_acc
    risk_adjusted = mit_acc - 0.5 * gap

    return rec_acc, mit_acc, gap, risk_adjusted, per_hazard


if __name__ == "__main__":
    print("model	recognition	mitigation	gap	risk_adjusted")
    for m in MODELS:
        rec, mit, gap, ra, _ = evaluate(m)
        print(f"{m:20s}	{rec:.3f}		{mit:.3f}		{gap:.3f}	{ra:.3f}")
