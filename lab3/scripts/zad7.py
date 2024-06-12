import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz

def multiply_matrix_vector(A, x):
    return A.dot(x)

def calculate_errors(x_approx, x_exact, A, b):
    solution_error = np.linalg.norm(x_approx - x_exact)
    residual_error = np.linalg.norm(b - A.dot(x_approx))
    return solution_error, residual_error

def perform_regularizations(A, b, x_exact, lambda_tikhonov, k_tsvd):
    # Tikhonov Regularization
    A_tilde = np.vstack((A, lambda_tikhonov * np.eye(A.shape[1])))
    b_tilde = np.concatenate((b, np.zeros(A.shape[1])))
    x_tikhonov = np.linalg.lstsq(A_tilde, b_tilde, rcond=None)[0]

    # TSVD Regularization
    U, sigma, VT = np.linalg.svd(A, full_matrices=False)
    sigma_truncated = np.zeros_like(sigma)
    sigma_truncated[:k_tsvd] = sigma[:k_tsvd]
    Sigma_truncated = np.diag(sigma_truncated)
    Sigma_truncated_inv = np.diag([1 / s if s > 0 else 0 for s in sigma_truncated])
    x_tsvd = VT.T @ Sigma_truncated_inv @ U.T @ b

    # Calculate and store errors
    solution_error, residual_error = calculate_errors(x_tikhonov, x_exact, A, b)

    return x_tikhonov, solution_error, residual_error

def estimate_rank_and_condition(A):
    rank_A = np.linalg.matrix_rank(A)
    cond_A = np.linalg.cond(A)
    return rank_A, cond_A

def plot_l_curve(A, b, x_exact, lambda_values, subplot_title):
    norms_solution = []
    norms_residual = []

    for lam in lambda_values:
        _, solution_error, residual_error = perform_regularizations(A, b, x_exact, lam, N)
        norms_solution.append(solution_error)
        norms_residual.append(residual_error)

    plt.loglog(norms_residual, norms_solution, label=subplot_title)
    plt.xlabel('Norma resztowa ||Ax-b||')
    plt.ylabel('Norma rozwiązania ||x-x*||')
    plt.grid(True)

def plot_l_curve_tsvd(A, b, x_exact, k_values, dataset_name):
    norms_solution = []
    norms_residual = []

    U, S, Vt = np.linalg.svd(A, full_matrices=False)

    for k in k_values:
        S_truncated = np.zeros_like(S)
        S_truncated[:k] = S[:k]
        Sigma_truncated_inv = np.diag(1 / S_truncated[:k])
        x_tsvd = Vt[:k, :].T @ Sigma_truncated_inv @ U[:, :k].T @ b

        solution_error, residual_error = calculate_errors(x_tsvd, x_exact, A, b)
        norms_solution.append(solution_error)
        norms_residual.append(residual_error)

    plt.loglog(norms_residual, norms_solution, label=f'TSVD for {dataset_name}')
    plt.xlabel('Norma resztowa (||Ax - b||)')
    plt.ylabel('Norma rozwiązania (||x-x*||)')
    plt.grid(True)

def plot_optimal_regularization_parameter(N_values):
    optimal_lambda_A = []
    optimal_lambda_B = []

    for N in N_values:
        # Generate Toeplitz matrix A
        c = np.arange(N)
        r = np.concatenate(([c[0]], -c[1:]))
        A = toeplitz(c, r)

        # Generate solutions x* for datasets (A) and (B)
        x_star_a = np.arange(1, N + 1)
        x_star_b = np.random.normal(0, 1, N)

        # Generate forward projections b for datasets (A) and (B)
        b_a = multiply_matrix_vector(A, x_star_a)
        b_b = multiply_matrix_vector(A, x_star_b)

        # Determine optimal lambda for dataset (A) - Placeholder
        optimal_lambda_A.append(np.argmin(
            [calculate_errors(perform_regularizations(A, b_a, x_star_a, lam, N)[0], x_star_a, A, b_a)[1] for lam in
             lambda_values]))

        # Determine optimal lambda for dataset (B) - Placeholder
        optimal_lambda_B.append(np.argmin(
            [calculate_errors(perform_regularizations(A, b_b, x_star_b, lam, N)[0], x_star_b, A, b_b)[1] for lam in
             lambda_values]))

    # Plotting the optimal lambda values
    plt.figure(figsize=(10, 6))
    plt.plot(N_values, optimal_lambda_A, 'o-', label='Optymalna wartość λ dla zbioru danych (A)')
    plt.plot(N_values, optimal_lambda_B, 's-', label='Optymalna wartość λ dla zbioru danych(B)')
    plt.xlabel('Wielkość macierzy N')
    plt.ylabel('Optymalna wartość parametru λ')
    plt.title('Optymalna wartość parametru λ w zależności od wielkości macierzy N')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main code section
lambda_values = np.logspace(-15, 1, 100)
N_values = [5, 10, 50, 100]

# Estimate and print rank and condition number for Toeplitz matrices of different sizes
for N in N_values:
    c = np.arange(N)
    r = np.concatenate(([c[0]], -c[1:]))
    A = toeplitz(c, r)
    rank_A, cond_A = estimate_rank_and_condition(A)
    print(f"N={N}: rank(A)={rank_A}, cond(A)={cond_A:.2e}")

# Create plots for the L-curve for data set (A) and (B) for N=10
N = 10
c = np.arange(N)
r = np.concatenate(([c[0]], -c[1:]))
A = toeplitz(c, r)

# Generate solutions x* for datasets (A) and (B)
x_star_a = np.arange(1, N + 1)
x_star_b = np.random.normal(0, 1, N)

# Forward projections b
b_a = multiply_matrix_vector(A, x_star_a)
b_b = multiply_matrix_vector(A, x_star_b)

k_values = range(1, min(A.shape) + 1)

plt.figure(figsize=(12, 6))

# Plot the L-curve for data set (A)
plt.subplot(1, 2, 1)
plot_l_curve(A, b_a, x_star_a, lambda_values, 'Zbiór danych (A)')

# Plot the L-curve for data set (B)
plt.subplot(1, 2, 2)
plot_l_curve(A, b_b, x_star_b, lambda_values, 'Zbiór danych (B)')

plt.suptitle('Krzywa L dla Regularyzacji Tichnowa')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

# Plot the L-curve for data set (A)
plt.subplot(1, 2, 1)
plot_l_curve_tsvd(A, b_a, x_star_a, k_values, 'Zbiór danych (A)')

# Plot the L-curve for data set (B)
plt.subplot(1, 2, 2)
plot_l_curve_tsvd(A, b_b, x_star_b, k_values, 'Zbiór danych (B)')

plt.suptitle('Krzywa L dla Regularyzacji TSVD')
plt.legend()
plt.tight_layout()
plt.show()

# Plot optimal regularization parameter as a function of N for datasets (A) and (B)
plot_optimal_regularization_parameter(N_values)
