from scipy.optimize import linprog
import numpy as np

# Define the A matrix
A = np.array([
    [2, 3, -1, 10, 21, 44, -9, 1, -1],
    [1, 2, 2, 8, 15, 35, 8, -3, 1],
    [3, 1, 1, 6, 16, 53, -7, 2, 2]
])

# Define the b vector (right-hand side of the constraints)
b = np.array([118, 77, 129])

# Define the bounds for the variables (p must be between 0 and 1)
bounds = [(0, 1), (None, None), (None, None), (None, None), (None, None), 
          (None, None), (None, None), (None, None), (None, None)]

# Objective function coefficients for minimizing sum of squared residuals
c = [0] * len(A[0])  # Objective function: minimize residuals for x

# Solve the linear optimization problem for p = 0
res_p0 = linprog(c, A_eq=A, b_eq=b, bounds=bounds)

# Update the bounds for p to be 1
bounds[0] = (1, 1)

# Solve the linear optimization problem for p = 1
res_p1 = linprog(c, A_eq=A, b_eq=b, bounds=bounds)

# Calculate the residual errors for p = 0
residuals_p0 = np.dot(A, res_p0.x) - b
error_p0 = np.sum(residuals_p0 ** 2)

# Calculate the residual errors for p = 1
residuals_p1 = np.dot(A, res_p1.x) - b
error_p1 = np.sum(residuals_p1 ** 2)

# Print the results
print("Results for p = 0:")
print("Optimal solution:", res_p0.x)
print("Residual error:", error_p0)

print("\nResults for p = 1:")
print("Optimal solution:", res_p1.x)
print("Residual error:", error_p1)

# Compare the residual errors
if error_p0 < error_p1:
    print("\nThe residual error is smaller for p = 0.")
elif error_p0 > error_p1:
    print("\nThe residual error is smaller for p = 1.")
else:
    print("\nThe residual errors are equal for p = 0 and p = 1.")
