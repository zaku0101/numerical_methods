import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


d = np.arange(0.1, 10.1, 0.1)
L = 128.3 + 32.51 * np.log10(d) + np.random.normal(0, 1, len(d))

def log_model(d, alpha, beta):
    return alpha + beta * np.log10(d)

def quadratic_model(d, alpha, beta, gamma):
    return alpha + beta * d + gamma * d**2

def cubic_model(d, alpha, beta, gamma, delta):
    return alpha + beta * d + gamma * d**2 + delta * d**3

# Fit models
popt_log, _ = curve_fit(log_model, d, L)
popt_quad, _ = curve_fit(quadratic_model, d, L)
popt_cubic, _ = curve_fit(cubic_model, d, L)

# Predict using fitted models
L_log_fit = log_model(d, *popt_log)
L_quad_fit = quadratic_model(d, *popt_quad)
L_cubic_fit = cubic_model(d, *popt_cubic)

# Plot the data and fitted models
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

# Output the parameters
print("Logarithmic Model parameters: alpha = {:.4f}, beta = {:.4f}".format(*popt_log))
print("Quadratic Model parameters: alpha = {:.4f}, beta = {:.4f}, gamma = {:.4f}".format(*popt_quad))
print("Cubic Model parameters: alpha = {:.4f}, beta = {:.4f}, gamma = {:.4f}, delta = {:.4f}".format(*popt_cubic))
