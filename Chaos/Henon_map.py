import matplotlib.pyplot as plt

# Constants
a = 1.4  # Parameter 'a' for the Hénon map
b = 0.3  # Parameter 'b' for the Hénon map
num_points = 10000  # Number of points to generate

# Initialize lists to store the x and y coordinates
x_values = []
y_values = []

# Initial conditions
x = 0.1
y = 0.1

# Generate points using the Hénon map
for _ in range(num_points):
    x_new = 1 - a * x * x + y
    y_new = b * x
    x, y = x_new, y_new
    x_values.append(x)
    y_values.append(y)

# Plot the Hénon map
plt.figure(figsize=(8, 8))
plt.scatter(x_values, y_values, s=1, c='b', marker='.')
plt.title("Hénon Map")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
