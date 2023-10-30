"""
Four Step Runge-Kutta method for ODEs.

This code covers an implicit four step Runge-Kutta method.
The code solves an initial value problem numerically.
"""

from datetime import datetime
import matplotlib.pyplot as plt
from math import exp, sqrt

__date__ = datetime(2022, 2, 11) # or version string or something
__author__ = "Ozhan Kayacan"


def Runge_Kutta(f, x0, y0, h):
    """
    Four step Runge-Kutta method (RK4) is implemented.
    The code solves first order ODEs
    """
    k0 = f(x0, y0)
    k1 = f(x0 + h/2, y0 + h/2 * k0)
    k2 = f(x0 + h/2, y0 + h/2 * k1)
    k3 = f(x0 + h, y0 + h * k2)

    k = (k0 + 2.0*k1 + 2.0*k2 + k3) / 6.0

    x1 = x0 + h
    y1 = y0 + h * k

    return x1, y1

def f(x, y):
    # First order ordinary differential equation (ODE)
    # You can use another first order ODE to solve.
    return (x**2-2*y) / (exp(2*x+y))

if __name__=="__main__":
    # Initial values
    x0 = 0.0
    y0 = 1.0

    # Step length
    h = 0.1

    x_values = [x0]
    y_values = [y0]

    # Calculate solution
    x = x0
    y = y0
    for _ in range(100):
        x, y = Runge_Kutta(f, x, y, h)
        x_values.append(x)
        y_values.append(y)
        print(x, y)


    # Plot solution

    # Solution is plotted as a function of steps.
    plt.plot(x_values, y_values)
    plt.show()