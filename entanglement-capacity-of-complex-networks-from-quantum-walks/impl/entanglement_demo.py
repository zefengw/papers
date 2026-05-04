
import numpy as np

def compute_source_target_entanglement(adj_matrix):
    # Simplified proxy: normalized Laplacian eigenvalues spread
    L = np.diag(adj_matrix.sum(axis=1)) - adj_matrix
    eigvals = np.linalg.eigvalsh(L)
    # Capacity bound calculation proxy
    capacity = np.sum(eigvals > 1e-5) / len(eigvals)
    return capacity

# Erdos-Renyi Graph
N = 10
p = 0.3
adj = (np.random.rand(N, N) < p).astype(float)
adj = np.maximum(adj, adj.transpose())
np.fill_diagonal(adj, 0)

cap = compute_source_target_entanglement(adj)
print(f"Network Entanglement Capacity Proxy: {cap:.4f}")
