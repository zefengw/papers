import numpy as np

class QLDPCSimulation:
    def __init__(self, n, m):
        # n = number of qubits, m = number of checks
        # Random binary parity check matrix H (mocking a high-rate construction)
        self.H = np.random.randint(0, 2, (m, n))
        self.n = n
        self.m = m

    def inject_errors(self, error_rate=0.01):
        # Random X-errors
        errors = np.random.choice([0, 1], size=self.n, p=[1-error_rate, error_rate])
        return errors

    def get_syndrome(self, errors):
        # Syndrome s = H * e (mod 2)
        return np.dot(self.H, errors) % 2

    def simple_decoder(self, syndrome):
        # Very basic decoder: find a vector 'e' that matches the syndrome
        # In reality, this would be Belief Propagation or a similar algorithm.
        # Here we just check if the original error vector matches (for demo).
        return "Syndrome computed. Decoding would now search for most likely e."

# Simulation
sim = QLDPCSimulation(n=2304, m=1152) # As per paper: [[2304, 1156]]
errors = sim.inject_errors()
syndrome = sim.get_syndrome(errors)

print(f"Qubit count: {sim.n}, Check count: {sim.m}")
print(f"Syndrome sample (first 10): {syndrome[:10]}")
print(sim.simple_decoder(syndrome))
