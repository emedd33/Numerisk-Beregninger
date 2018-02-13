from sympy import sin, symbols, series, exp
from sympy.utilities.lambdify import lambdify
import numpy as np
import matplotlib.pyplot as plt

def Problem2():
    t,x = symbols('t x')
    f = exp(t)
    expr = series(f, t, 0, 5)
    expr = expr.removeO()
    print('')
    print('Taylor expansion of f(t) = exp(t) around t=0')
    print(expr)

    func = sin(x)
    N=100
    for i in range(2,7):

        expr = series(func,x,0,i*2)
        expr = expr.removeO()
        taylorEval = lambdify(x, expr, 'numpy')
        x = np.linspace(0, 2 * np.pi, N)
        plt.plot(x, taylorEval(x))
        x = symbols('x')

    plt.ylim([-2.0, 2.0])
    plt.xlim([0.0, 2 * np.pi])
    x = np.linspace(0, 2 * np.pi, N)
    plt.plot(x, np.sin(x))
    plt.legend(
        ['series, N = 4', 'series, N = 6', 'series, N = 8', 'series, N = 10', 'series, N = 12', 'series, N = 14'])
    plt.show()