import numpy as np

class AtManRLSaliency:
    def __init__(self, sequence_length, vocab_size):
        self.seq_len = sequence_length
        self.vocab_size = vocab_size
        # Mock attention weights [seq_len, seq_len]
        self.attention_weights = np.random.dirichlet(np.ones(sequence_length), size=sequence_length)

    def get_saliency_reward(self, tokens, correct_answer):
        # Simplified saliency: sum of attention weights of tokens that 'matter'
        # In reality, this is differentiable via the attention mask.
        
        # Assume tokens 1 to seq_len-1 are CoT, token seq_len is the answer.
        cot_tokens = tokens[:-1]
        answer_token = tokens[-1]
        
        # Saliency of CoT tokens relative to the answer token
        saliency_scores = self.attention_weights[-1, :-1]
        
        # Reward is higher if the 'correct' reasoning path had higher saliency
        # Mock: tokens that match the 'gold' reasoning path get higher weight
        gold_path = [1, 0, 1, 1, 0] # Mock gold pattern
        
        if len(cot_tokens) != len(gold_path):
            return 0.0
            
        reward = np.sum(saliency_scores * np.array(gold_path))
        return reward

# Simulation
sim = AtManRLSaliency(6, 100)
mock_tokens = [10, 20, 30, 40, 50, 99] # 5 CoT + 1 Answer
reward = sim.get_saliency_reward(mock_tokens, 99)
print(f"Saliency Reward: {reward:.4f}")
