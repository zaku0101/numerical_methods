import numpy as np
import matplotlib.pyplot as plt

# Define the Rosenbrock function
def rosenbrock(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

# Define the gradient of the Rosenbrock function
def rosenbrock_grad(x):
    dfdx1 = -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0])
    dfdx2 = 200 * (x[1] - x[0]**2)
    return np.array([dfdx1, dfdx2])

# Steepest descent algorithm
def steepest_descent(rosenbrock, rosenbrock_grad, x0, learning_rate=0.001, max_iter=100000, tol=1e-6):
    x = x0
    for i in range(max_iter):
        grad = rosenbrock_grad(x)
        x_new = x - learning_rate * grad
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
    return x, rosenbrock(x), i

# Initial points
initial_points = [np.array([1.2, 1.2]), np.array([-1.2, 1.0])]

# Perform steepest descent for each initial point
results = []
for x0 in initial_points:
    result = steepest_descent(rosenbrock, rosenbrock_grad, x0)
    results.append(result)

# Display results
for idx, (x0, (x_min, f_min, iterations)) in enumerate(zip(initial_points, results)):
    print(f"Initial point {idx+1}: {x0}")
    print(f"Minimum found at: {x_min}")
    print(f"Function value at minimum: {f_min}")
    print(f"Iterations: {iterations}")
    print()

# Plot contour plot
x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)
Z = 100 * (Y - X**2)**2 + (1 - X)**2

plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 20), cmap='jet')
for x0 in initial_points:
    plt.plot(x0[0], x0[1], 'ro')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.colorbar()
plt.show()