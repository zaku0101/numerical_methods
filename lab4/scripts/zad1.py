import numpy as np

def focuss(A, b, params):
  # Extract parameters
  lambda_ = params["lambda"]
  max_iter = params["max_iter"]
  tol = params["tol"]

  # Get dimensions
  m, n = A.shape

  # Initialize estimated source signals
  x_hat = np.zeros(n)

  # Iteration loop
  for i in range(max_iter):
    # Soft thresholding step
    thresh = lambda_ * np.sqrt(np.sum(x_hat**2, axis=0))
    x_hat = np.sign(x_hat) * np.maximum(np.abs(x_hat) - thresh, 0)

    # Update using least squares with diagonal weighting matrix
    W = np.diag(1 / (np.abs(x_hat) + 1e-6))  # Avoid division by zero
    try:
        x_hat = np.linalg.solve(A.T @ W @ A, A.T @ W @ b)  # Check for `np.linalg.solve`
    except np.linalg.LinAlgError as e:
        print(f"Error during solving least squares: {e}")
        # Consider handling potential convergence issues here

    # Check for convergence
    if np.linalg.norm(x_hat - np.copy(x_hat)) < tol:
      print(f"Converged after {i+1} iterations.")
      break

  return x_hat

# Define your mixed signal values (replace with your actual values)
a = 5
b = 2
c = -1

# Define the mixing matrix (assuming you have it defined)
A = np.array([[1, 3, 1], [-1, -2, 1], [3, 7, -1]])

# Define algorithm parameters
params = {
  "lambda": 0.1,
  "max_iter": 100,
  "tol": 1e-6
}

# Call the FOCUSS function
x_hat = focuss(A, np.array([a, b, c]), params)
print("Estimated source signals:", x_hat)
