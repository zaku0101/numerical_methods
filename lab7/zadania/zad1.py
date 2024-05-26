import numpy as np
import matplotlib.pyplot as plt

# Definicja funkcji Rosenbrocka
def rosenbrock(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

# Punkt, w którym sprawdzamy warunki optymalizacji
punkt = np.array([1, 1])

# Gradient funkcji Rosenbrocka
def gradient_rosenbrock(x):
    return np.array([-400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0]), 
                     200 * (x[1] - x[0]**2)])

# Sprawdzenie warunków pierwszego rzędu
grad = gradient_rosenbrock(punkt)
print(f"Gradient w punkcie {punkt}: {grad}")

# Rysowanie wykresu konturowego
x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)
Z = rosenbrock([X, Y])

plt.figure(figsize=(6, 4))
plt.contour(X, Y, Z, levels=np.logspace(-0.5, 3.5, 20), cmap='jet')
plt.plot(1, 1, 'ro') # Punkt optymalny
plt.title('Wykres konturowy funkcji Rosenbrocka')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
