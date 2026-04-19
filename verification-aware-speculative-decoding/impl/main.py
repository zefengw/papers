
import torch
import torch.nn as nn

class SimpleLM(nn.Module):
    def __init__(self, vocab_size, dim):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, dim)
        self.linear = nn.Linear(dim, vocab_size)
    def forward(self, x):
        return self.linear(self.embed(x))

def speculative_decode(drafter, verifier, input_ids, max_steps=5):
    vocab_size = drafter.linear.out_features
    current_ids = input_ids
    
    for _ in range(max_steps):
        # Drafter proposes a 'step' (sequence of tokens)
        with torch.no_grad():
            logits = drafter(current_ids)
            next_token = torch.argmax(logits[:, -1, :], dim=-1).unsqueeze(-1)
            proposal = torch.cat([current_ids, next_token], dim=-1)
            
            # Verifier checks the proposal
            v_logits = verifier(proposal)
            v_next_token = torch.argmax(v_logits[:, -2, :], dim=-1).unsqueeze(-1)
            
            if torch.equal(next_token, v_next_token):
                current_ids = proposal
                print(f"Step accepted: {next_token.item()}")
            else:
                print(f"Step rejected. Verifier correction: {v_next_token.item()}")
                current_ids = torch.cat([current_ids, v_next_token], dim=-1)
                break
    return current_ids

if __name__ == '__main__':
    vocab_size, dim = 100, 32
    drafter = SimpleLM(vocab_size, dim)
    verifier = SimpleLM(vocab_size, dim * 2) # Simulation of a larger model
    # Adjust verifier to be 'smarter' for demo
    with torch.no_grad():
        verifier.linear.weight.copy_(torch.randn(vocab_size, dim * 2))
        
    input_ids = torch.tensor([[1, 2, 3]])
    result = speculative_decode(drafter, verifier, input_ids)
    print("Final sequence:", result)
