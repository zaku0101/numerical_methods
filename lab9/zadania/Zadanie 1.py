import numpy as np
import matplotlib.pyplot as plt

# Definicja okręgu
theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(2)
x1 = r * np.cos(theta)
x2 = r * np.sin(theta)

# Punkty optymalne
opt_points = np.array([[-1, -1], [1, 1]])

# Rysowanie wykresu
plt.figure(figsize=(8, 8))
plt.plot(x1, x2, label='$x_1^2 + x_2^2 = 2$')

# Zaznaczenie punktów optymalnych
plt.scatter(opt_points[:,0], opt_points[:,1], color='red', zorder=5)
for point in opt_points:
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', fontsize=12, ha='right')

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
