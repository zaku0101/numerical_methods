import numpy as np

# Define the matrix A and the vector x for Task 1
A = np.array([[1, 2, 2, 3, 1],
              [2, 4, 4, 6, 2],
              [3, 6, 6, 9, 6],
              [1, 2, 4, 5, 3]])
x = np.array([1, 0, 1, 1])

# Perform the QR decomposition of A (Task 1: Finding projection)
Q, R = np.linalg.qr(A)

# Calculate the projection of x onto the column space of A using the QR decomposition (Task 1)
proj = Q @ (Q.T @ x)

# Print the projection (Task 1)
print("The projection of x onto the column space of A is:")
print(proj)

# Now, define the vector b for Task 2
b = proj  # Using the projection as b for Task 2

# Solve the original equation Ax = b using least squares (Task 2: Finding approximate solution)
x_original, residuals_original, rank_original, s_original = np.linalg.lstsq(A, b, rcond=None)

# Modify the matrix A by changing a_21 from 2 to 0 (Task 2: Modifying the matrix)
A_modified = A.copy()
A_modified[1, 0] = 0

# Solve the modified equation Ax = b using least squares (Task 2: Re-estimating the solution)
x_modified, residuals_modified, rank_modified, s_modified = np.linalg.lstsq(A_modified, b, rcond=None)

# Calculate the error between the original and modified solutions (Task 2)
error = np.linalg.norm(x_original - x_modified)

# Calculate the residual for the original solution (Task 2)
residual_original_vector = b - A @ x_original

# Calculate the residual for the modified solution (Task 2)
residual_modified_vector = b - A_modified @ x_modified

# Print the results for Task 2
print("Original solution:", x_original)
print("Modified solution:", x_modified)
print("Error between solutions:", error)
print("Residual for original solution:", residual_original_vector)
print("Residual for modified solution:", residual_modified_vector)