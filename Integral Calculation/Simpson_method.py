import numpy as np


def f(x):
    # Define the function you want to integrate here.
    return x ** 2


def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be an even integer.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral


# Define the limits of integration and the number of subintervals (n)
a = 0.0
b = 1.0
n = 4  # You can adjust n for desired accuracy

result = simpsons_rule(f, a, b, n)
print("Approximate integral:", result)
