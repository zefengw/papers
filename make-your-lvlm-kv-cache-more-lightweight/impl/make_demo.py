
import torch
import torch.nn as nn

def lightkv_compress(vision_tokens, text_prompts, ratio=0.5):
    # vision_tokens: [B, N_v, D], text_prompts: [B, N_t, D]
    # Compute importance based on text prompt alignment
    importance = torch.matmul(vision_tokens, text_prompts.mean(dim=1, keepdim=True).transpose(-1, -2))
    importance = importance.squeeze(-1) # [B, N_v]
    
    k = int(vision_tokens.size(1) * ratio)
    _, indices = torch.topk(importance, k, dim=1)
    
    # Pruned KV cache representation
    compressed = torch.stack([vision_tokens[b][indices[b]] for b in range(vision_tokens.size(0))])
    return compressed

# Toy test
v_tokens = torch.randn(1, 100, 128)
t_prompts = torch.randn(1, 10, 128)
comp = lightkv_compress(v_tokens, t_prompts)
print(f"Original: {v_tokens.size(1)}, Compressed: {comp.size(1)}")
