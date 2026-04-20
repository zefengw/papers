import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def simulate_learning(mode='reward', steps=100, lr=0.1):
    # Initial distribution (logits)
    logits = np.random.randn(5)
    history = []
    
    # Target index (the "correct" answer)
    target = 2
    
    for i in range(steps):
        prob = softmax(logits)
        history.append(prob.copy())
        
        if mode == 'reward':
            # Reward-based: Gradient of log-prob of target
            # Grad = (1 - prob[target]) for target, -prob[j] for others
            grad = -prob
            grad[target] += 1
            logits += lr * grad
        elif mode == 'sharpening':
            # Sharpening: Move towards a sharp target distribution (one-hot)
            # Target is just a high-peak at the mode, regardless of "reward"
            # Simulating as increasing the gap between max and others
            target_dist = np.zeros(5)
            target_dist[np.argmax(prob)] = 1.0
            
            # Gradient to match target_dist (KL divergence approx)
            grad = target_dist - prob
            logits += lr * grad
            
    return np.array(history)

# Compare
reward_hist = simulate_learning(mode='reward')
sharp_hist = simulate_learning(mode='sharpening')

print("Final Distribution (Reward):", softmax(reward_hist[-1]))
print("Final Distribution (Sharpening):", softmax(sharp_hist[-1]))

# Note: In a real scenario, sharpening might peak on the WRONG token if it's the current mode.
# Reward-based RL peaks on the CORRECT token.
