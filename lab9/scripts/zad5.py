import cvxpy as cp

# Definiowanie zmiennych
x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()

# Funkcja celu
objective = cp.Minimize(x1**2 + x2**2 + x3**2)

# Ograniczenia
constraints = [
    x1 + 2*x2 - x3 == 4,
    x1 - x2 + x3 == -2
]

# Definiowanie problemu
problem = cp.Problem(objective, constraints)

# Rozwiązywanie problemu
problem.solve()

# Wyświetlanie wyników
print("Optymalne wartości zmiennych:")
print("x1 =", x1.value)
print("x2 =", x2.value)
print("x3 =", x3.value)
print("Minimalna wartość funkcji celu =", problem.value)
