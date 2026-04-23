
import numpy as np

def continuous_diffusion_forward(x_0, t, noise_schedule):
    beta = noise_schedule(t)
    alpha = 1.0 - beta
    alpha_hat = np.prod(alpha)
    noise = np.random.randn(*x_0.shape)
    x_t = np.sqrt(alpha_hat) * x_0 + np.sqrt(1.0 - alpha_hat) * noise
    return x_t
