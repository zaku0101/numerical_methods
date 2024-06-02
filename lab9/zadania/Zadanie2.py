import numpy as np
import matplotlib.pyplot as plt

# Definicja okręgu
theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(2)
x1 = r * np.cos(theta)
x2 = r * np.sin(theta)

# Zbiór dopuszczalny
x1_range = np.linspace(-2, 2, 400)
x2_range = np.linspace(-2, 2, 400)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)
feasible_region = (x2_grid >= 0) & (2 - x1_grid**2 - x2_grid**2 >= 0)

# Punkty optymalne
opt_points = np.array([[-np.sqrt(2), 0], [np.sqrt(2), 0]])

# Rysowanie wykresu
plt.figure(figsize=(8, 8))
plt.contourf(x1_grid, x2_grid, feasible_region, levels=[0, 1], colors=['lightgray'], alpha=0.5)
plt.plot(x1, x2, label='$x_1^2 + x_2^2 = 2$')

# Zaznaczenie punktów optymalnych
plt.scatter(opt_points[:,0], opt_points[:,1], color='red', zorder=5)
for point in opt_points:
    plt.text(point[0], point[1], f'({point[0]:.2f}, {point[1]:.2f})', fontsize=12, ha='right')

# Ustawienia wykresu
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Zbiór rozwiązań dopuszczalnych i punkty spełniające warunki KKT')
plt.axis('equal')
plt.show()
