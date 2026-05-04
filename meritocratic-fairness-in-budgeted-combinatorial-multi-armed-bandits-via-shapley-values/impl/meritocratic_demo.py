
import numpy as np

def k_shapley_approximation(arms, k, valuation_fn, samples=100):
    n = len(arms)
    scores = np.zeros(n)
    for _ in range(samples):
        perm = np.random.permutation(n)
        for i in range(n):
            idx = perm[i]
            pre = perm[:i]
            # Restriction to set of size at most K
            if len(pre) < k:
                scores[idx] += valuation_fn(np.append(pre, idx)) - valuation_fn(pre)
    return scores / samples

def simple_val(subset):
    return np.sqrt(len(subset)) # Concave mock valuation

arms = np.arange(10)
sh_vals = k_shapley_approximation(arms, 3, simple_val)
print(f"Arm 0 Shapley: {sh_vals[0]:.4f}, sum: {sh_vals.sum():.4f}")
