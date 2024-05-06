from pulp import LpMinimize, LpProblem, LpVariable, lpSum, value

# Inicjalizacja problemu
prob = LpProblem("Diet Problem", LpMinimize)

# Definicja zmiennych decyzyjnych (ilość sera i chleba do zakupu w kg)
x1 = LpVariable("Sera_kg", lowBound=0)  # ilość sera w kg
x2 = LpVariable("Chleba_kg", lowBound=0)  # ilość chleba w kg

# Definicja funkcji celu (minimalizacja kosztów)
prob += 30 * x1 + 20 * x2, "Koszt"

# Definicja ograniczeń dotyczących białka i węglowodanów
prob += 20 * x1 + 10 * x2 >= 60, "Białko"
prob += 20 * x1 + 30 * x2 >= 120, "Węglowodany"

# Rozwiązanie problemu
prob.solve()

# Wyświetlenie wyników
print("Status:", prob.status)
print("Koszt najbardziej ekonomicznej diety:", value(prob.objective), "zł")
print("Ilość sera:", value(x1), "kg")
print("Ilość chleba:", value(x2), "kg")
