import numpy as np
from problem1.py import analyticalSol
import scipy
import scipy.sparse
import scipy.sparse.linalg

def initializeSolution(N):
    """ Function that creates an initial guess Y0 of the solution y(x) to the ODE given in Problem 1.
        This is needed to start the iteration process in the linearization solvers to be implemented.
        We choose Y0 to be a straight line from the boundaries, y(xmin) to y(xmax)

        Args:
            N (int): number of unknowns

        Returns:
            x (array): discretized domain. Array with length (N + 2)
            Y0 (array): straight line between [y(xmin), y(xmax)]. Array with length (N + 2).

    """

    # YOUR CODE HERE

    x = np.linspace(0, 0.9, N + 2)
    y_analytical = analyticalSol(x)
    y0, yEnd = y_analytical[0], y_analytical[-1]
    Y0 = np.linspace(y0, yEnd, N + 2)  # initial guess

    return x, Y0


def simpleLinearization(N, itMax, tol=1e-3):
    """ Function that solves the BVP:
            y''(x) = -2*x*(y''(x))^2,
            y(0) = 2, y(0.9) = [ln(0.1) - ln (1.9)] + 2 =~ 0.52778,
        Using central difference discretization and the proposed linearization.

        Args:
            N (int): number of unknowns
            itMax (int): maximum number of iterations
            tol (float): tolerance limit for the infinity norm (defaults to 1e-3)

        Returns:
            Y (array): solution array with length (N + 2).

    """

    # YOUR CODE HERE
    x, Y0 = initializeSolution(N)
    y_analytical = analyticalSol(x)
    y0, yEnd = Y0[0], Y0[-1]
    h = x[1] - x[0]
    x_unknown = x[1:-1]  # all x-values except BC's

    for n in range(itMax):

        Y0Plus = Y0[2:]
        Y0Minus = Y0[0:-2]
        d = -0.5 * x_unknown * (Y0Plus - Y0Minus) ** 2
        d[0] = d[0] - y0
        d[-1] = d[-1] - yEnd

        A = scipy.sparse.diags([1, -2, 1], [-1, 0, 1], shape=(N, N), format='csc')

        Y1 = scipy.sparse.linalg.spsolve(A, d)

        Y1Full = np.append(y0, Y1)
        Y1Full = np.append(Y1Full, yEnd)

        Y0 = Y1Full

        epsilon = np.max(np.abs(y_analytical - Y0))
        if epsilon < tol:
            print("tolerance criteria is met, it: {0}, epsilon: {1}".format(n + 1, epsilon))
            break

    Y = Y1Full

    return Y


def newtonLinearization(N, itMax, tol=1e-3):
    """ Function that solves the BVP:
            y''(x) = -2*x*(y''(x))^2,
            y(0) = 2, y(0.9) = [ln(0.1) - ln (1.9)] + 2 =~ 0.52778,
        Using central difference discretization and newton linearization.

        Args:
            N (int): number of unknowns
            itMax (int): maximum number of iterations
            tol (float): tolerance limit for the infinity norm (defaults to 1e-3)

        Returns:
            Y (array): solution array with length (N + 2).

    """

    # YOUR CODE HERE
    x, Y0 = initializeSolution(N)
    y_analytical = analyticalSol(x)
    y0, yEnd = Y0[0], Y0[-1]
    h = x[1] - x[0]
    x_unknown = x[1:-1]  # all x-values except BC's

    for n in range(itMax):

        Y0Plus = Y0[2:]
        Y0Minus = Y0[0:-2]
        alpha = Y0Plus - Y0Minus

        MainDiag = -2 * np.ones(N)
        supDiag = 1 + x_unknown[:-1] * alpha[:-1]
        subDiag = 1 - x_unknown[1:] * alpha[1:]
        d = 0.5 * x_unknown * (alpha) ** 2
        d[0] = d[0] - y0 * (1 - x_unknown[0] * alpha[0])
        d[-1] = d[-1] - yEnd * (1 + x_unknown[-1] * alpha[-1])

        A = scipy.sparse.diags([subDiag, MainDiag, supDiag], [-1, 0, 1], format='csc')

        Y1 = scipy.sparse.linalg.spsolve(A, d)

        Y1Full = np.append(y0, Y1)
        Y1Full = np.append(Y1Full, yEnd)

        Y0 = Y1Full

        epsilon = np.max(np.abs(y_analytical - Y0))

        if epsilon < tol:
            print("tolerance criteria is met, it: {0}, epsilon: {1}".format(n + 1, epsilon))
            break

    Y = Y1Full

    return Y