# Concept: Sequential vs Simultaneous Entanglement Swapping Coherence Simulation
# Approximates the decay of entanglement fidelity based on memory coherence time and swapping strategy.

import math

def simulate_swapping(chain_length=4, coherence_time=100, heralding_latency=10, strategy="simultaneous"):
    base_fidelity = 0.99
    
    if strategy == "simultaneous":
        # All swaps happen ASAP, less time lingering in memory
        time_in_memory = heralding_latency
    elif strategy == "sequential":
        # Partial chains held in memory waiting for adjacent swaps
        # Scales with chain length
        time_in_memory = heralding_latency * (chain_length - 1)
        
    # Coherence penalty
    ratio = coherence_time / time_in_memory
    
    if ratio < 1.0:
        penalty = math.exp(-1/ratio) # steep dropoff if coherence < memory time
    else:
        penalty = 1.0 - (1/ratio) * 0.1 # gradual penalty
        
    final_fidelity = base_fidelity * penalty
    return max(0.0, final_fidelity)

print("Sweeping Coherence Time / Heralding Latency Ratios:\n")
latency = 10
for coherence in [10, 50, 250, 1000, 5000]:
    ratio = coherence / latency
    sim_fid = simulate_swapping(coherence_time=coherence, heralding_latency=latency, strategy="simultaneous")
    seq_fid = simulate_swapping(coherence_time=coherence, heralding_latency=latency, strategy="sequential")
    print(f"Ratio: {ratio:5.1f} | Simultaneous Fidelity: {sim_fid:.3f} | Sequential Fidelity: {seq_fid:.3f}")
    if ratio < 25 and seq_fid < 0.1:
        print("  -> Sequential hit severe coherence threshold collapse.")
