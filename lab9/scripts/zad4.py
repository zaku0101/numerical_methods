import cvxpy as cp

# Zdefiniowane zmienne
x1 = cp.Variable()
x2 = cp.Variable()

# Funkcja celu (do zminimalizowania)
objective = cp.Minimize(x1**2 + x2**2 - 4*x1 - 2*x2 - 6)

# Ograniczenia
constraints = [x1 + x2 <= 2, -x1 + 2*x2 <= 2, 2*x1 + x2 <= 2, x1 >= 0, x2 >= 0]

# Problem programowania kwadratowego
prob = cp.Problem(objective, constraints)

# Rozwiązanie problemu
prob.solve()

# Wyświetlenie wyników
print("Wartość minimalna funkcji:", prob.value)
print("x1:", x1.value)
print("x2:", x2.value)
