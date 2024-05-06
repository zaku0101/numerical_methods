import numpy as np
import matplotlib.pyplot as plt

# Funkcja celu
def objective_function(x1, x2):
    return x1 + x2

# Ograniczenia
def constraint1(x1):
    return (4 - x1) / 2

def constraint2(x1):
    return (12 - 4*x1) / 2

def constraint3(x1):
    return 1 + x1

# Tworzenie siatki punktów
x1_values = np.linspace(0, 3, 400)
x2_values = np.linspace(0, 3, 400)
x1_mesh, x2_mesh = np.meshgrid(x1_values, x2_values)

# Sprawdzenie, które punkty spełniają wszystkie ograniczenia
feasible_region = (x1_mesh + 2*x2_mesh <= 4) & (4*x1_mesh + 2*x2_mesh <= 12) & (-x1_mesh + x2_mesh <= 1) & (x1_mesh >= 0) & (x2_mesh >= 0)

# Wybór punktu optymalnego
optimal_point = np.unravel_index(np.argmax(objective_function(x1_mesh[feasible_region], x2_mesh[feasible_region])), feasible_region.shape)

# Wartości optymalne x1 i x2
optimal_x1 = x1_values[optimal_point[1]]
optimal_x2 = x2_values[optimal_point[0]]

# Rysowanie wykresu
plt.figure(figsize=(8, 6))
plt.contourf(x1_mesh, x2_mesh, feasible_region, cmap='Blues', alpha=0.5)
plt.colorbar(label="Feasible Region")
plt.plot(x1_values, constraint1(x1_values), label=r"$x_1 + 2x_2 \leq 4$", color='red')
plt.plot(x1_values, constraint2(x1_values), label=r"$4x_1 + 2x_2 \leq 12$", color='green')
plt.plot(x1_values, constraint3(x1_values), label=r"$-x_1 + x_2 \leq 1$", color='orange')
plt.xlim(0, 3)
plt.ylim(0, 3)
plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")
plt.title("Feasible Region and Objective Function")
plt.scatter(optimal_x1, optimal_x2, color='red', label="Optimal Point")
plt.legend()
plt.grid(True)
plt.show()

print("Optimal solution:")
print("x1 =", optimal_x1)
print("x2 =", optimal_x2)
print("Maximum objective value:", objective_function(optimal_x1, optimal_x2))
