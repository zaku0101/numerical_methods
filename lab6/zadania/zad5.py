import pulp

# Inicjalizacja problemu
prob = pulp.LpProblem("Maximize Returns", pulp.LpMaximize)

# Zmienne decyzyjne
x1 = pulp.LpVariable("Obligacje", lowBound=0)  # Inwestycja w fundusz obligacji
x2 = pulp.LpVariable("Depozyt", lowBound=0)  # Inwestycja w lokatę bankową
x3 = pulp.LpVariable("Wysokie ryzyko", lowBound=0, upBound=2000)  # Inwestycja w konto wysokiego ryzyka

# Funkcja celu - maksymalizacja zwrotów
prob += 0.07 * x1 + 0.08 * x2 + 0.12 * x3, "Total_Returns"

# Ograniczenia
prob += x1 >= 3 * x2  # Inwestycja w obligacje komunalne musi być co najmniej trzy razy większa niż w lokatę bankową
prob += x1 + x2 + x3 <= 12000  # Suma inwestycji nie może przekroczyć 12000 USD

# Rozwiązanie problemu
prob.solve()

# Wyświetlenie wyników
print("Optymalne kwoty:")
for v in prob.variables():
    print(v.name, "=", "${:,.2f}".format(v.varValue))

print("Szacowana stopa zwrotu = ${:,.2f}".format(pulp.value(prob.objective)))

