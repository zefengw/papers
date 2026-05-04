
import numpy as np

def cvqe_prob_analysis(state_vector):
    probs = np.abs(state_vector)**2
    entropy = -np.sum(probs * np.log(probs + 1e-12))
    return probs, entropy

# Simulating a 4-qubit state
state = np.random.randn(16) + 1j * np.random.randn(16)
state /= np.linalg.norm(state)
probs, ent = cvqe_prob_analysis(state)
print(f"Max Prob: {np.max(probs):.4f}, Base Entropy: {ent:.4f}")
