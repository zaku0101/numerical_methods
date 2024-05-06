from scipy.optimize import linprog
import numpy as np


def pivot_on(A, row, col):
    # Get the pivot element
    pivot = A[row, col]
    # Scale the pivot row to make the pivot element 1
    A[row, :] /= pivot
    # Perform row operations to make all other elements in the pivot column 0
    for r in range(A.shape[0]):
        if r != row:
            A[r, :] -= A[r, col] * A[row, :]


def find_pivot(A):
    # Column selection: choose the smallest index where the entry in the last row is negative (minimization)
    col = np.argmin(A[-1, :-1])
    if A[-1, col] >= 0:
        return -1, -1  # No more negative entries, optimal solution found

    # Row selection: choose the row with the smallest positive ratio of rhs to the column entry
    ratios = np.array([A[r, -1] / A[r, col] if A[r, col] > 0 else np.inf for r in range(A.shape[0] - 1)])
    row = np.argmin(ratios)
    if ratios[row] == np.inf:
        return -1, -1  # Unbounded

    return row, col


def custom_linprog(c, A_ub, b_ub, bounds):
    num_vars = len(c)

    # Create the tableau
    tableau = np.zeros((len(A_ub) + 1, len(A_ub[0]) + len(A_ub) + 1))

    # Set up the objective function in the tableau (last row)
    tableau[-1, :num_vars] = -np.array(c)

    # Set up the constraints in the tableau
    for i in range(len(A_ub)):
        tableau[i, :num_vars] = A_ub[i]
        tableau[i, num_vars + i] = 1
        tableau[i, -1] = b_ub[i]

    # Perform the Simplex algorithm
    while True:
        row, col = find_pivot(tableau)
        if row == -1 or col == -1:
            break
        pivot_on(tableau, row, col)

    if np.min(tableau[-1, :-1]) < 0:
        return None  # No solution found (could be unbounded)

    # Extract solution
    solution = np.zeros(num_vars)
    for i in range(num_vars):
        if np.sum(tableau[:, i] == 1) == 1 and np.sum(tableau[:, i] != 0) == 1:
            solution[i] = tableau[np.where(tableau[:, i] == 1)[0], -1]

    return solution, tableau[-1, -1]

def simplex(c, A, b, bounds, maximize=False):
    """
    Solve linear programming problems.

    Parameters:
        c (list of floats): Coefficients of the objective function.
        A (list of lists of floats): Coefficient matrix for inequality constraints.
        b (list of floats): Right-hand side vector for inequality constraints.
        bounds (list of tuples): Bounds for each variable.
        maximize (bool): True if the objective is to maximize, False for minimize.

    Returns:
        str: Description of the solution or error message.
    """
    # If the objective is to maximize, convert it to minimize by negating the objective coefficients
    if maximize:
        c = [-i for i in c]

    # Solve the problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

    if res.success:
        if maximize:
            objective_value = -res.fun
        else:
            objective_value = res.fun
        return f"Optymalnymi wartościami funkcji jest {objective_value} w {' '.join(f'x{i + 1} = {x:.4f}' for i, x in enumerate(res.x))}"
    else:
        return "No feasible solution found."