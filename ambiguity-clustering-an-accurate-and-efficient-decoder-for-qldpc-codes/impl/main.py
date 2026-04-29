# Ambiguity Clustering Core Logic
def identify_clusters(syndrome, bp_posteriors):
    # Find qubits with high entropy (ambiguous)
    # Group connected ambiguous qubits into clusters
    clusters = []
    # ... traversal logic ...
    return clusters

def decode_ac(syndrome, bp_results):
    clusters = identify_clusters(syndrome, bp_results)
    corrections = []
    for c in clusters:
        # Solve cluster-local maximum likelihood problem
        res = solve_local_ml(c)
        corrections.append(res)
    return merge(corrections)
