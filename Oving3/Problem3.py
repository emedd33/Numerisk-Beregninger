from sympy import sin, symbols, diff, integrate, solve, series, exp
from sympy.utilities.lambdify import lambdify
import numpy as np
import matplotlib.pyplot as plt


def Problem3_method(N):
    P, E, I, L = 1.0, 1.0, 1.0, 1.0
    K = P / (E * I)

    N = 100
    x = np.linspace(0,L,N)
    h = x[1] - x[0]

    y0_0 = -(K * L ** 3) / (3.0)
    y1_0 = (K * L ** 2) / (2.0)

    y = np.zeros((2,N))
    y[0, 0] = y0_0
    y[1, 0] = y1_0
    for n in range(N - 1):
        y0_n = y[0, n]
        y1_n = y[1, n]

        y[0, n + 1] = y0_n + h * y1_n
        y[1, n + 1] = y1_n + h * (-K * x[n])
    plt.figure(2)
    Euler = y[0, :]
    plt.plot(x, Euler)


    # Heuns
    for n in range(N - 1):
        y0_n = y[0, n]
        y1_n = y[1, n]


        y0_p = y0_n + h * y1_n
        y1_p = y1_n + h * (-K * x[n])

        y[0, n + 1] = y0_n + (h / 2.0) * (y1_n + y1_p)
        y[1, n + 1] = y1_n + (h / 2.0) * (-2 * K * x[n])
    heun = y[0, :]

    analytical_sol = (K / 6.0) * (-x ** 3 + 3 * L ** 2 * x - 2 * L ** 3)

    plt.plot(x, heun)
    plt.plot(x, analytical_sol)

    r = 2.0
    x = np.linspace(0, 1, 5)




def Problem3():
    N = 100
    Problem3_method(N)

    plt.xlim([0.0, 1.0])
    plt.legend(['Euler', 'Heun', 'Analytical'])
    plt.show()
