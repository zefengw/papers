# DAPO Clipping Logic
import torch

def dapo_loss(prob_ratio, advantages, clip_eps=0.2, clip_upper_eps=0.5):
    # Decoupled Clip: Widen the upper bound for positive advantages
    # to allow the policy to move toward better trajectories more aggressively
    surr1 = prob_ratio * advantages
    
    # Asymmetric clipping
    clipping = torch.where(
        advantages > 0,
        torch.clamp(prob_ratio, 1 - clip_eps, 1 + clip_upper_eps),
        torch.clamp(prob_ratio, 1 - clip_eps, 1 + clip_eps)
    )
    surr2 = clipping * advantages
    return -torch.min(surr1, surr2).mean()
