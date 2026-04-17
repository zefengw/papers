#!/usr/bin/env python3
"""Minimal IOC -> regex operationalization demo."""
import re


def infer_type(ioc: str) -> str:
    if re.fullmatch(r"[0-9a-fA-F]{64}", ioc):
        return 'sha256'
    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", ioc):
        return 'ipv4'
    if '.' in ioc and '/' not in ioc:
        return 'domain'
    if ioc.startswith(('http://', 'https://')):
        return 'url'
    return 'literal'


def ioc_to_regex(ioc: str) -> str:
    t = infer_type(ioc)
    if t == 'sha256':
        return r"\b[0-9a-fA-F]{64}\b"
    if t == 'ipv4':
        return r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    if t == 'domain':
        return r"\b(?:[a-zA-Z0-9-]+\.)+[A-Za-z]{2,}\b"
    if t == 'url':
        return r'https?://[^\s\'\"]+'
    return re.escape(ioc)


def evaluate(pattern: str, positives, negatives):
    rgx = re.compile(pattern)
    hit = sum(1 for x in positives if rgx.search(x)) / max(1, len(positives))
    fp = sum(1 for x in negatives if rgx.search(x)) / max(1, len(negatives))
    return hit, fp


def main() -> None:
    ioc = 'evil-update.example'
    pattern = ioc_to_regex(ioc)

    positives = [
        'dns query for evil-update.example seen',
        'beacon to cdn.evil-update.example',
        'related host: billing.evil-update.example',
    ]
    negatives = [
        'benign request to docs.python.org',
        'connect to intranet.local',
        'hash value abcdef not a domain'
    ]

    hit, fp = evaluate(pattern, positives, negatives)
    print('IOC:', ioc)
    print('Detected type:', infer_type(ioc))
    print('Regex:', pattern)
    print(f'Hit rate: {hit:.3f}')
    print(f'False positive rate: {fp:.3f}')


if __name__ == '__main__':
    main()
