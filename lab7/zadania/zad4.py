import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Definicja funkcji Himmelblaua
def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

# Znane minima
minima = np.array([
    [3, 2],
    [-3.78, -3.28],
    [-2.81, 3.13],
    [3.58, -1.85]
])

# Generowanie punktów siatki startowej
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
start_points = np.c_[X.ravel(), Y.ravel()]

# Algorytmy do zastosowania
methods = ['BFGS', 'CG']

# Funkcja do przypisania wyników do najbliższego znanego minimum
def classify_minimum(result, minima):
    distances = np.linalg.norm(minima - result, axis=1)
    return np.argmin(distances)

# Przeprowadzenie optymalizacji
results = {method: np.zeros_like(X, dtype=int) for method in methods}

for method in methods:
    for idx, point in enumerate(start_points):
        res = minimize(himmelblau, point, method=method)
        classified_min = classify_minimum(res.x, minima)
        results[method].ravel()[idx] = classified_min

# Wizualizacja wyników osobno dla każdej metody
for method in methods:
    plt.figure(figsize=(7, 7))
    c = plt.pcolormesh(X, Y, results[method], shading='auto')
    plt.scatter(minima[:, 0], minima[:, 1], c='red', marker='x')
    plt.title(f'Rezultaty dla metody {method}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar(c, ticks=[0, 1, 2, 3], label='Minimum')
    plt.show()
