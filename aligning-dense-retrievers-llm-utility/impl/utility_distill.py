
import torch
import torch.nn.functional as F

def utility_aware_loss(query_embed, doc_embed, llm_utility_score, scale=1.0):
    # query_embed: [B, D], doc_embed: [B, D]
    # llm_utility_score: [B] (0 to 1, how much the doc helped the LLM)
    cosine_sim = F.cosine_similarity(query_embed, doc_embed)
    
    # We want cosine_sim to be high when llm_utility_score is high
    loss = F.mse_loss(cosine_sim, llm_utility_score * scale)
    return loss

if __name__ == "__main__":
    q = torch.randn(1, 128)
    d = torch.randn(1, 128)
    u = torch.tensor([0.9]) # LLM says this doc was very useful
    loss = utility_aware_loss(q, d, u)
    print(f"Utility alignment loss: {loss.item()}")
