
import numpy as np

def generate_parity_check(n, k, weight):
    # Dummy placeholder for hypergraph product / TS code generation
    H = np.zeros((n - k, n), dtype=int)
    for i in range(n - k):
        indices = np.random.choice(n, weight, replace=False)
        H[i, indices] = 1
    return H
