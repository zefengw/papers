
import random

def syndrome_decoder(qubit_states, bias="Z"):
    """
    Handles 'loss-biased' noise where one type of error 
    (e.g., phase Z or loss) is much more frequent.
    """
    syndromes = []
    for state in qubit_states:
        # Simulate biased error
        if random.random() < 0.1:
            syndromes.append(f"Error {bias} detected")
    return syndromes

if __name__ == "__main__":
    qubits = [0] * 10
    print("Detected Syndromes:", syndrome_decoder(qubits))
