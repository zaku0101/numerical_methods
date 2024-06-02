import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Generowanie danych zgodnie z modelem
c = 3  # Stała wartość c zgodnie z zadaniem
d = np.arange(0.1, 10.1, 0.1)
L = 128.3 + 32.51 * np.log10(d) + c  # Dodajemy stałą wartość c

# Definicje modeli
def log_model(d, alpha, beta):
    return alpha + beta * np.log10(d)

def quadratic_model(d, alpha, beta, gamma):
    return alpha + beta * d + gamma * d**2

def cubic_model(d, alpha, beta, gamma, delta):
    return alpha + beta * d + gamma * d**2 + delta * d**3

# Dopasowanie modeli do danych
popt_log, _ = curve_fit(log_model, d, L)
popt_quad, _ = curve_fit(quadratic_model, d, L)
popt_cubic, _ = curve_fit(cubic_model, d, L)

# Predykcja przy użyciu dopasowanych modeli
L_log_fit = log_model(d, *popt_log)
L_quad_fit = quadratic_model(d, *popt_quad)
L_cubic_fit = cubic_model(d, *popt_cubic)

# Wykres danych i dopasowanych modeli
plt.figure(figsize=(10, 6))
plt.scatter(d, L, label='Dane', color='black')
plt.plot(d, L_log_fit, label='Model logarytmiczny', color='red')
plt.xlabel('Dystans (d) [km]')
plt.ylabel('Tłumienie (L) [dB]')
plt.legend()
plt.title('Dopasowanie modeli tłumienia do danych')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(d, L, label='Dane', color='black')
plt.plot(d, L_quad_fit, label='Model kwadratowy', color='blue')
plt.xlabel('Dystans (d) [km]')
plt.ylabel('Tłumienie (L) [dB]')
plt.legend()
plt.title('Dopasowanie modeli tłumienia do danych')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(d, L, label='Dane', color='black')
plt.plot(d, L_cubic_fit, label='Model trzeciego stopnia', color='green')
plt.xlabel('Dystans (d) [km]')
plt.ylabel('Tłumienie (L) [dB]')
plt.legend()
plt.title('Dopasowanie modeli tłumienia do danych')
plt.show()

# Wyświetlenie parametrów
print("Parametry modelu logarytmicznego: alpha = {:.4f}, beta = {:.4f}".format(*popt_log))
print("Parametry modelu kwadratowego: alpha = {:.4f}, beta = {:.4f}, gamma = {:.4f}".format(*popt_quad))
print("Parametry modelu trzeciego stopnia: alpha = {:.4f}, beta = {:.4f}, gamma = {:.4f}, delta = {:.4f}".format(*popt_cubic))
