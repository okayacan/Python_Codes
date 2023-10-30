import numpy as np
import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
num_iterations = 1000  # Number of iterations for each r value
num_r_values = 1000    # Number of different r values to explore
r_values = np.linspace(2.4, 4.0, num_r_values)  # Range of r values to explore
initial_x = 0.5       # Initial value of x

# Create an array to store the bifurcation diagram
bifurcation = []

# Iterate over different r values
for r in r_values:
    x = initial_x
    for _ in range(num_iterations):
        x = logistic_map(r, x)
        if _ >= num_iterations // 2:
            bifurcation.append([r, x])

# Separate r and x values for plotting
r_values_plot, x_values = zip(*bifurcation)

# Plot the bifurcation diagram
plt.figure(figsize=(10, 6))
plt.scatter(r_values_plot, x_values, s=0.1, c='blue', marker='.')
plt.title("Logistic Map Bifurcation Diagram")
plt.xlabel("r Values")
plt.ylabel("x Values")
plt.xlim(2.4, 4.0)
plt.grid()
plt.show()
