import numpy as np

# Definicja wektorów y i x
y = np.array([3, 0, -1, 2])
x = np.array([0, 1, 1, -1])

# Transpozycja dwóch wektorów
y = y.reshape(-1, 1)
x = x.reshape(-1, 1)

# Tworzenie macierzy A
A = np.hstack((np.ones_like(x), x**2, np.sin(np.pi * x / 2)))

# Obliczenie z1
z1 = np.linalg.inv(A.T @ A) @ A.T @ y

print(z1)