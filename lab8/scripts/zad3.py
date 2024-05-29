import numpy as np
from scipy.optimize import fsolve

# Define the system of nonlinear equations
def equations(vars):
    x1, x2 = vars
    eq1 = 2 * x1 - x2 - np.exp(-x1)
    eq2 = -x1 + 2 * x2 - np.exp(-x2)
    return [eq1, eq2]

# Initial guess
x0 = [-5, -5]

# Solve the system of equations
solution = fsolve(equations, x0)

# Print the solution
print("Solution:")
print(f"x1 = {solution[0]}")
print(f"x2 = {solution[1]}")