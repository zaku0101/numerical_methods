import timeit
from algos import *


c = [1, 1]  # Coefficients for the objective function including slack variables
A = [[1, 2], [4, 2], [-1, 1]]  # Coefficient matrix for inequalities with slack variables
b = [4, 12, 1]  # Right-hand side for inequalities
bounds = [(0, None), (0, None)]  # Bounds for each variable, including slack variables
start_custom = timeit.default_timer()
print(custom_linprog(c, A, b, bounds))
stop_custom = timeit.default_timer()

start_simplex = timeit.default_timer()
print(simplex(c, A, b, bounds, maximize=True))
stop_simplex = timeit.default_timer()
print("Custom time: ", stop_custom - start_custom)
print("Simplex time: ", stop_simplex - start_simplex)