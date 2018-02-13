from sympy import symbols, diff, integrate, solve
import numpy as np
import matplotlib.pyplot as plt

def Problem1():
    v0, t, g = symbols('v0 t g')
    y = v0*t-0.5*g*np.power(t,2);
    vt = diff(y, t)
    at = diff(vt, t)
    y2 = integrate(vt, t)
    print('y(t),v(t),a(t),y_2')
    print(y)
    print(vt)
    print(at)
    print(y2)

    roots = solve(y, t)
    print('')
    print('Roots of the function')
    print(roots)

    v0 = np.array(5)
    g = np.array(9.81)
    y = v0 * t - 0.5 * g * t ** 2
    rootsNum = solve(y, t)
    t0 = float(rootsNum[0])
    tend = float(rootsNum[1])
    t = np.linspace(t0, tend, 100)
    y = v0 * t - 0.5 * g * t ** 2

    plt.figure(1)
    plt.plot(t, y)
    plt.show()