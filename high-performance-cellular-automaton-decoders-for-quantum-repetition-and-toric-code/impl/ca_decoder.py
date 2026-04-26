
import numpy as np

class CellularAutomatonDecoder:
    def __init__(self, size):
        self.size = size
        self.state = np.zeros((size, size), dtype=int)
        
    def step(self, syndromes):
        # Simplified CA rule: flip if syndrome is present and parity allows
        new_state = self.state.copy()
        for i in range(self.size):
            for j in range(self.size):
                if syndromes[i, j] == 1:
                    new_state[i, j] = 1 - self.state[i, j]
        self.state = new_state

# Simulation
size = 5
decoder = CellularAutomatonDecoder(size)
rand_syndromes = np.random.randint(0, 2, (size, size))
decoder.step(rand_syndromes)
print(f"Final CA state shape: {decoder.state.shape}")
