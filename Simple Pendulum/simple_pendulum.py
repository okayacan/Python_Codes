import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
length = 1.0  # Length of the pendulum (m)
initial_angle = math.radians(30)  # Initial angle in radians
time_step = 0.01  # Time step for simulation (seconds)
total_time = 10  # Total simulation time (seconds)

# Initialize arrays to store time and angle values
time_values = np.arange(0, total_time, time_step)
angle_values = []

# Simulate the pendulum motion using simple harmonic motion formula
for t in time_values:
    angle = initial_angle * math.cos(math.sqrt(g / length) * t)
    angle_values.append(angle)

# Convert angles from radians to degrees for plotting
angle_degrees = [math.degrees(angle) for angle in angle_values]

# Plot the pendulum motion
plt.plot(time_values, angle_degrees)
plt.title("Simple Pendulum Motion")
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.grid()
plt.show()