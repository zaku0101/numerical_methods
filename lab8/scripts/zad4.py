import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(x):
    x1, x2 = x
    total = 0
    for k in range(1, 11):
        total += (2 + 2*k - np.exp(k*x1) - np.exp(k*x2))**2
    return total

# Initial guess
x0 = [0.3, 0.4]

# Minimize the objective function
result = minimize(objective, x0)

# Print the solution
print("Solution:")
print(f"x1 = {result.x[0]}")
print(f"x2 = {result.x[1]}")