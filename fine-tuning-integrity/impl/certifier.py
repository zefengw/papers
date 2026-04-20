import numpy as np

class DriftCertifier:
    def __init__(self, base_weights):
        self.base_weights = base_weights

    def compute_delta(self, tuned_weights):
        return tuned_weights - self.base_weights

    def certify_sparsity(self, delta, threshold):
        # Count non-zero elements
        non_zeros = np.count_nonzero(delta)
        is_valid = non_zeros <= threshold
        return is_valid, f"Non-zeros: {non_zeros}, Threshold: {threshold}"

    def certify_norm(self, delta, threshold):
        # Frobenius norm
        norm = np.linalg.norm(delta)
        is_valid = norm <= threshold
        return is_valid, f"Norm: {norm:.4f}, Threshold: {threshold}"

    def certify_rank(self, delta, threshold):
        # Singular Value Decomposition for rank
        s = np.linalg.svd(delta, compute_uv=False)
        rank = np.sum(s > 1e-5)
        is_valid = rank <= threshold
        return is_valid, f"Rank: {rank}, Threshold: {threshold}"

# Test
np.random.seed(42)
base = np.random.randn(10, 10)
# Simulate a low-rank update (LoRA-like)
u = np.random.randn(10, 2)
v = np.random.randn(2, 10)
delta = u @ v
tuned = base + delta

cert = DriftCertifier(base)
d = cert.compute_delta(tuned)

print("Sparsity Check:", cert.certify_sparsity(d, 100)) # Likely fail
print("Norm Check:", cert.certify_norm(d, 10.0))       # May pass
print("Rank Check:", cert.certify_rank(d, 2))          # Should pass
