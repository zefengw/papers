#!/usr/bin/env python3
"""Simple reliability dashboard inspired by GPT-4 style reporting."""

from collections import defaultdict


def pass_at_k(n_samples, n_correct, k):
    if n_correct == 0:
        return 0.0
    if n_samples - n_correct < k:
        return 1.0

    numer = 1.0
    denom = 1.0
    for i in range(k):
        numer *= (n_samples - n_correct - i)
        denom *= (n_samples - i)
    return 1.0 - (numer / denom)


def expected_calibration_error(preds, n_bins=5):
    bins = defaultdict(list)
    for conf, correct in preds:
        idx = min(n_bins - 1, int(conf * n_bins))
        bins[idx].append((conf, correct))

    total = len(preds)
    ece = 0.0
    for i in range(n_bins):
        if not bins[i]:
            continue
        avg_conf = sum(c for c, _ in bins[i]) / len(bins[i])
        avg_acc = sum(y for _, y in bins[i]) / len(bins[i])
        ece += (len(bins[i]) / total) * abs(avg_conf - avg_acc)
    return ece


def refusal_metrics(samples):
    tp = sum(1 for s in samples if s['unsafe'] and s['refused'])
    fp = sum(1 for s in samples if (not s['unsafe']) and s['refused'])
    fn = sum(1 for s in samples if s['unsafe'] and (not s['refused']))

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    return precision, recall


def main():
    n, c = 20, 7
    p1 = pass_at_k(n, c, k=1)
    p5 = pass_at_k(n, c, k=5)

    preds = [
        (0.95, 1), (0.90, 1), (0.85, 0), (0.82, 1),
        (0.70, 1), (0.65, 0), (0.60, 1), (0.58, 0),
        (0.45, 1), (0.35, 0), (0.25, 0), (0.10, 0),
    ]
    ece = expected_calibration_error(preds, n_bins=5)

    safety_samples = [
        {'unsafe': True, 'refused': True},
        {'unsafe': True, 'refused': True},
        {'unsafe': True, 'refused': False},
        {'unsafe': False, 'refused': False},
        {'unsafe': False, 'refused': True},
        {'unsafe': False, 'refused': False},
    ]
    precision, recall = refusal_metrics(safety_samples)

    print('=== Reliability dashboard (toy) ===')
    print(f'pass@1: {p1:.4f}')
    print(f'pass@5: {p5:.4f}')
    print(f'ECE (5 bins): {ece:.4f}')
    print(f'Refusal precision: {precision:.4f}')
    print(f'Refusal recall: {recall:.4f}')


if __name__ == '__main__':
    main()
