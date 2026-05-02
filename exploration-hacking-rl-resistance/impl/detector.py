import torch
import torch.nn as nn
import numpy as np

class ExplorationHackingDetector(nn.Module):
    """
    Detects potential exploration hacking by monitoring strategy shifts 
    in action entropy and activation distribution.
    """
    def __init__(self, activation_dim, threshold=0.1):
        super().__init__()
        self.threshold = threshold
        self.running_mean_activation = None
        
    def detect_entropy_collapse(self, logits):
        """
        Calculates Shannon entropy of logits. 
        Sudden drops in entropy may indicate the model is trying to 'hide' 
        exploration by consistently picking low-signal paths.
        """
        probs = torch.softmax(logits, dim=-1)
        entropy = -torch.sum(probs * torch.log(probs + 1e-10), dim=-1)
        return entropy

    def detect_activation_anomaly(self, activations):
        """
        Compares current activations to running mean.
        Strategic resistance often triggers specific sub-networks.
        """
        current_mean = torch.mean(activations, dim=0)
        if self.running_mean_activation is None:
            self.running_mean_activation = current_mean.detach()
            return 0.0
        
        diff = torch.norm(current_mean - self.running_mean_activation)
        # Update running mean slowly
        self.running_mean_activation = 0.99 * self.running_mean_activation + 0.01 * current_mean.detach()
        return diff.item()

if __name__ == "__main__":
    detector = ExplorationHackingDetector(activation_dim=128)
    # Mock data: 1 batch, 10 sequence length, 50 vocab size
    mock_logits = torch.randn(1, 10, 50)
    mock_activations = torch.randn(10, 128)
    
    entropy = detector.detect_entropy_collapse(mock_logits)
    anomaly_score = detector.detect_activation_anomaly(mock_activations)
    
    print(f"Mean Entropy: {entropy.mean().item():.4f}")
    print(f"Activation Anomaly Score: {anomaly_score:.4f}")
