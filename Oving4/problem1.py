
import matplotlib.pylab as plt
import numpy as np

def discretizeX(xmin, xmax, N):
    """ function that discretizes x from xmin to xmax into N points

        Args:
            xmin (float): start position of discretization
            xmax (float): end position of discretization
            N (int): number of points in the discretized domain

        Returns:
            x (array): discretized domain with length N

    """

    # YOUR CODE HERE
    x = np.linspace(xmin,xmax,N)
    return x



#TEST!!
xmin = 0
xmax = 0.9
N = 91
x = discretizeX(xmin, xmax, N)



def analyticalSol(x):
    """ Function that calculates the analytical expression
        y(x) = (ln|x - 1| - ln|x + 1|)/2 + 2, x in [0,0.9]

        Args:
            x (array): a vector of points/positions x

        Returns:
            y_analytical (array): y(x)

    """

    # YOUR CODE HERE
    y_analytical = (np.log(np.abs(x - 1)) - np.log(np.abs(x + 1)))/2 + 2
    return y_analytical


# Here we call the function that you have implemented.
# Note that we use the "x" vector defined in cell (1).
# So variables defined in one cell are available in successive cells!

#TEST!!
#x= np.linspace(0,0.9,10)
#y_analytical = analyticalSol(x)


def dYfunc(x, Y):
    """ Function that calculates the derivatives of the system of first order ODEs obtained from the second order ODE
        y''(x) = -2*x*(y'(x))^2

        Args:
            x (float): current position x_i
            Y (list/array): solutions at point x_i, [y(x_i), y'(x_i)]

        Returns:
            dY (array): derivatives at point x_i, [y'(x_i), y''(x_i)]

    """

    # YOUR CODE HERE

    dY = np.array([Y[1], -2 * x * Y[1] ** 2])
    return dY


def Heun(x, Y_0, dYfunc):
    """ General implementation of Heuns's method that takes a vector x, a set of initial conditions Y_0 and
        and a function dyFunc (see 1c) as inputs and solves a system of ODE's.

        Args:
            x (array): discretized domain
            Y_0 (list/array): initial values. e.g. [y(xmin), y'(xmin)]
            dYfunc (function): function that calculates the derivatives of the system, e.g. ([y'(x_i), y''(x_i)])

        Returns:
            Y (array): Solution array of shape (len(x), len(Y_0))
    """

    # YOUR CODE HERE
    Y = np.zeros((len(x),len(Y_0)))
    Y[0,:] = Y_0

    for i in range(len(x[0:-1])):
        dx = x[i+1]-x[i]
        Yp = Y[i,:] + dx*dYfunc(x[i],Y[i,:])
        Y[i+1,:] = Y[i,:] + dx/2*(dYfunc(x[i+1],Yp)+dYfunc(x[i],Y[i,:]))

    return Y[:, [0, 1]]


def shoot(x, itMax, s0=-0.5, s1=-0.6, tol=1e-3):
    """ Function that solves the BVP:
        y''(x) = -2*x*(y'(x))^2
        y(0) = 2, y(0.9) = [ln(0.1) - ln (1.9)] + 2 =~ 0.52778,
        using Heun's method and shooting technique.

        Args:
            x (array): discretized domain
            itMax (int): maximum number of iterations
            s0 (float): first guess of the initialvalue s=y'(x_min). Defaults to -0.5
            s1 (float): second guess of the initialvalue s=y'(x_min). Defaults to -0.6
            tol (float): tolerance limit for the infinity norm. Defaults to 1e-3

        Returns:
            Y (array): solution array of y(x), with same length as x

    """
    # YOUR CODE HERE
    y_analytical = analyticalSol(x)

    beta = 0.52778  # y_analytical[-1] #0.52778

    Y_0 = [2, s0]
    Y = Heun(x, Y_0, dYfunc)[:, 0]  # extract only y(x), not y'(x)

    phi0 = Y[-1] - beta
    for it in range(itMax):
        # solve using shooting technique

        Y_0 = [2, s1]
        Y = Heun(x, Y_0, dYfunc)[:, 0]
        phi1 = Y[-1] - beta
        ds = -phi1 * (s1 - s0) / float(phi1 - phi0)
        s0 = s1
        s1 = s1 + ds
        phi0 = phi1

        epsilon = np.max(np.abs(y_analytical - Y))

        if epsilon < tol:
            print("tolerance criteria is met, it: {0}, epsilon: {1}".format(it + 1, epsilon))
            break
    return Y
