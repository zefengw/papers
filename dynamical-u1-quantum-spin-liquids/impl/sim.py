import numpy as np

def simulate_u1_dynamics(steps=100):
    """
    Toy simulation of U(1) gauge dynamics on a small lattice.
    Focuses on the evolution of gauge invariant quantities.
    """
    # Simple 2x2 lattice of plaquettes
    state = np.random.rand(4) 
    history = []
    
    for i in range(steps):
        # Unitary-like evolution of gauge fields
        state = (state + 0.1 * np.sin(state)) % (2 * np.pi)
        history.append(np.mean(np.cos(state)))
    
    return history

if __name__ == "__main__":
    results = simulate_u1_dynamics()
    print(f"Simulation finished. Final average flux: {results[-1]}")
