from pulp import *

# Definicja problemu
problem = LpProblem("Zrównoważona normalna dieta")

# Zmienne decyzyjne
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# Funkcja celu
problem += 30 * x + 20 * y, LpMinimize

# Ograniczenia
problem += 20 * x + 10 * y >= 60
problem += 20 * x + 30 * y >= 120

# Rozwiązanie problemu
problem.solve()

# Wyświetlenie wyników
print("Ilość sera:", x.value())
print("Ilość chleba:", y.value())
print("Koszt diety:", problem.objective.value())
