import numpy as np
import matplotlib.pyplot as plt

# Definiowanie funkcji celu
def objective_function(x1, x2):
    return x1**2 + x2**2

# Definiowanie ograniczenia
def constraint(x1, x2):
    return x1 + x2 - 1

# Tworzenie siatki punktów dla x1 i x2
x1 = np.linspace(-2, 2, 400)
x2 = np.linspace(-2, 2, 400)
X1, X2 = np.meshgrid(x1, x2)
Z = objective_function(X1, X2)
C = constraint(X1, X2)

# Zbiór dopuszczalny (constraint >= 0)
feasible_region = C >= 0

# Punkt optymalny
optimal_point = (0.5, 0.5)

# Rysowanie wykresu
plt.figure(figsize=(8, 8))
plt.contour(X1, X2, Z, levels=50, cmap='jet', alpha=0.5)
plt.contourf(X1, X2, feasible_region, levels=[0, 1], colors=['lightgray'], alpha=0.3)
plt.plot(optimal_point[0], optimal_point[1], 'ro', label=f'Optimum (x1, x2) = {optimal_point}')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Zbiór rozwiązań dopuszczalnych i punkt optymalny')
plt.legend()
plt.grid(True)
plt.show()
