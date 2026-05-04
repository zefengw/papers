
import numpy as np

def pvm_sim(x, visual_memory):
    # Simulated Persistent Visual Memory
    # x: query, visual_memory: keys
    scores = np.dot(x, visual_memory.T)
    weights = np.exp(scores) / np.sum(np.exp(scores), axis=-1, keepdims=True)
    retrieved = np.dot(weights, visual_memory)
    gate = 0.5 # constant gate
    return x + gate * retrieved

x = np.random.randn(1, 128)
v_mem = np.random.randn(5, 128)
out = pvm_sim(x, v_mem)
print(f"PVM Output Shape: {out.shape}")
