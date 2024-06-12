import numpy as np
import matplotlib.pyplot as plt

# Funkcja f(x)
def f(x):
  return np.pi**2 - x**2

# Funkcja g(x)
def g(x, n, c):
  sum = 0
  for j in range(n+1):
    sum += c[j] * np.cos(j*x)
  return sum

# Minimalizacja błędu
def minimize_error(n):
  # Współczynniki c
  c = np.zeros(n+1)

  # Macierz A
  A = np.zeros((n+1, n+1))
  for i in range(n+1):
    for j in range(n+1):
      A[i, j] = np.cos(i*j)

  # Wektor b
  b = np.zeros(n+1)
  for i in range(n+1):
    b[i] = f(i*np.pi/n)

  # Rozwiązanie układu równań
  c = np.linalg.solve(A, b)

  # Obliczenie błędu
  error = 0
  for i in range(n+1):
    error += (f(i*np.pi/n) - g(i*np.pi/n, n, c))**2

  return error

for n in range(1, 11):
  # Współczynniki c
  c = np.zeros(n+1)

  # Macierz A
  A = np.zeros((n+1, n+1))
  for i in range(n+1):
    for j in range(n+1):
      A[i, j] = np.cos(i*j)

  # Wektor b
  b = np.zeros(n+1)
  for i in range(n+1):
    b[i] = f(i*np.pi/n)

  # Rozwiązanie układu równań
  c = np.linalg.solve(A, b)


# Błędy
for n in range(1, 11):
  error = minimize_error(n)
  print(f"n={n}, błąd={error}")
