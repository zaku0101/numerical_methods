from scipy.optimize import minimize
import numpy as np

# Define the objective function
def objective(x):
    return x[0]**2 - x[1]**2

# Define the constraints
def constraint1(x):
    return x[0] + 2*x[1] - 2

def constraint2(x):
    return -5*x[0] + 4*x[1] - 10

# Define the bounds manually since COBYLA doesn't support bounds directly
def cobyla_bounds(x):
    return [x[0], -x[0], x[1]]

# Define the initial guess
x0 = [-0.1, 1.0]  # Feasible initial guess

# Define the constraints dictionary
cons = [{'type': 'ineq', 'fun': constraint1},
        {'type': 'ineq', 'fun': constraint2},
        {'type': 'ineq', 'fun': lambda x: x[0]},    # x1 <= 0 --> x1 is negative
        {'type': 'ineq', 'fun': lambda x: x[1]}]    # x2 >= 0 --> x2 is positive

# Solve the problem
solution = minimize(objective, x0, method='COBYLA', constraints=cons)

# Print the results
print(f"Optimal value: {solution.fun}")
print(f"Optimal x1: {solution.x[0]}")
print(f"Optimal x2: {solution.x[1]}")