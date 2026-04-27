
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

def f(n_d):
    # Simulated scaling law: L(N, D) = a/N^alpha + b/D^beta + c
    return 10 / (n_d[0]**0.3) + 20 / (n_d[1]**0.2) + 0.5

def active_experiment_selection(budget, bounds):
    configs = []
    losses = []
    
    # Start with initial grid
    for n in [bounds['n'][0], bounds['n'][1]]:
        for d in [bounds['d'][0], bounds['d'][1]]:
            configs.append([n, d])
            losses.append(f([n, d]))
    
    kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
    
    for _ in range(budget):
        gp.fit(configs, losses)
        # Search for configuration with max uncertainty (Simple active selection)
        search_n = np.linspace(bounds['n'][0], bounds['n'][1], 50)
        search_d = np.linspace(bounds['d'][0], bounds['d'][1], 50)
        N, D = np.meshgrid(search_n, search_d)
        candidates = np.array([N.flatten(), D.flatten()]).T
        
        y_pred, sigma = gp.predict(candidates, return_std=True)
        best_candidate = candidates[np.argmax(sigma)]
        
        configs.append(best_candidate)
        losses.append(f(best_candidate))
        
    return configs, losses

if __name__ == "__main__":
    bounds = {'n': (1e6, 1e9), 'd': (1e7, 1e11)}
    configs, losses = active_experiment_selection(budget=10, bounds=bounds)
    print(f"Selected {len(configs)} configurations for scaling law fitting.")
