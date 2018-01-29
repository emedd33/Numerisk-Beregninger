"""Eulers methor:
y_1+1 = y_1 + h*f(x_1,y_1)

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import special


def plotXY(X, Y):
    plt.plot(X, Y)
    plt.ylabel("function value")
    plt.xlabel("variable value of function")
    plt.legend()
    plt.show()


def function(N):
    Y = [0]
    X = [0]
    h = 1.5 / N

    for i in range(N):
        Y_app = Y[i] + h * func(X[i], Y[i])
        Y.append(Y_app)
        X.append(X[i] + h)
    return Y, X


def func(X, Y):
    return 1 - 3 * X + Y + np.power(X, 2) + X * Y


def NewtonSol(N):
    X = [0]
    h = 1.5 / N
    Y = [0]
    for i in range(N):
        Y_app = X[i] - np.power(X[i], 2) + np.power(X[i], 3) / 3 - np.power(X[i], 4) / 6 + np.power(X[i],
                                                                                                    5) / 30 - np.power(
            X[i], 6) / 45
        Y.append(Y_app)
        X.append(X[i] + h)
    return X, Y


def ExactSol(N):
    X = [0]
    h = 1.5 / N
    Y = [0]
    for i in range(N):
        y_t1 = np.exp(X[i] * (1 + X[i] / 2.0))
        y_t2 = special.erf((np.sqrt(2) / 2.0) * (1 + X[i])) - special.erf(np.sqrt(2) / 2.0)
        y_t3 = 1 - np.exp(X[i] * (1 + X[i] / 2.0))
        Y.append(3 * np.sqrt(2 * np.pi * np.exp(1)) * y_t1 * y_t2 + 4 * y_t3 - X[i])
        X.append(X[i]+h)

    return X, Y
