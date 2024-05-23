import numpy as np
import matplotlib.pyplot as plt



# Generowanie siatki punktów
x = np.linspace(-50, 50, 1000)
y = np.linspace(-50, 50, 1000)
X, Y = np.meshgrid(x, y)
Z = 2*X**2 - X*Y + 0.5*Y**2 - 3*X + 3.5

# Tworzenie wykresu konturowego
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour)

# Dodanie etykiet i tytułu
plt.title('Wykres konturowy funkcji $f(x) = 2x_1^2 - x_1x_2 + \\frac{1}{2}x_2^2 - 3x_1 + 3.5$')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')

# Wyświetlenie wykresu
plt.show()

Z = -1.5*X**2 + X*Y - 0.5*Y**2 + 2*X - 1

# Tworzenie wykresu konturowego
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour)

# Dodanie etykiet i tytułu
plt.title('Wykres konturowy funkcji $f(x) = -\\frac{3}{2}x_1^2 + x_1x_2 - \\frac{1}{2}x_2^2 - 2x_1 - 1$')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')

# Wyświetlenie wykresu
plt.show()

Z = X**2 + 8*X*Y + 0.5*Y**2 - 10*X -9*Y - 4.5

# Tworzenie wykresu konturowego
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour)

# Dodanie etykiet i tytułu
plt.title('Wykres konturowy funkcji $f(x) = x_1^2 - 8x_1x_2 + \\frac{1}{2}x_2^2 - 10x_1 -9x_2 + 4.5$')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')

# Wyświetlenie wykresu
plt.show()
