def f(x):
    # Define the function you want to integrate here.
    return x**2

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    integral = h * (0.5 * y[0] + sum(y[1:-1]) + 0.5 * y[-1])
    return integral

# Define the limits of integration and the number of subintervals (n)
a = 0.0
b = 1.0
n = 4  # You can adjust n for desired accuracy

result = trapezoidal_rule(f, a, b, n)
print("Approximate integral:", result)
