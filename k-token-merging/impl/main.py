
import torch
import torch.nn.functional as F

def token_merging(x, k=2):
    # x: (batch, seq_len, dim)
    b, s, d = x.shape
    if s <= k: return x
    
    # Compute similarity matrix
    sim = F.cosine_similarity(x.unsqueeze(1), x.unsqueeze(2), dim=-1) # (b, s, s)
    
    merged_x = []
    for i in range(b):
        batch_sim = sim[i]
        # Simple greedy merging: merge most similar pairs
        mask = torch.ones(s, dtype=torch.bool)
        new_tokens = []
        
        # This is a very simplified version of the paper's merging
        while mask.sum() > k:
            # Find max similarity among active tokens
            active_indices = torch.where(mask)[0]
            if len(active_indices) <= 1: break
            
            # Sub-matrix of similarities
            sub_sim = batch_sim[active_indices][:, active_indices]
            # Mask diagonal
            sub_sim.fill_diagonal_(-1)
            
            # Find max pair
            max_idx = torch.argmax(sub_sim)
            row, col = divmod(max_idx.item(), len(active_indices))
            
            # Merge tokens
            idx1, idx2 = active_indices[row], active_indices[col]
            merged_token = (x[i, idx1] + x[i, idx2]) / 2
            new_tokens.append(merged_token)
            
            mask[idx1] = False
            mask[idx2] = False
            
        # Add remaining tokens
        remaining = x[i][mask]
        new_tokens.extend(remaining)
        merged_x.append(torch.stack(new_tokens))
        
    return torch.stack(merged_x) if len(merged_x) > 0 else x

if __name__ == '__main__':
    x = torch.randn(1, 10, 32)
    out = token_merging(x, k=4)
    print("Original shape:", x.shape)
    print("Merged shape:", out.shape)
