import numpy as np
import scipy
import scipy.sparse
import scipy.sparse.linalg
N = 5
A = scipy.sparse.diags([1, 2, 3], [-1, 0, 1], shape=(N, N), format='csc') # format='csc' works well with scipy.sparse.linalg.spsolve
A_numpy = A.toarray() # convert to numpy array

def SytemOfEquations(N):
    beta2 = 4
    h = 1./(N+1)



    x_i = np.linspace(0,N+1,N+2)

    mainDiag = -beta2*h-x_i[1:-1]*2
    subDiag = x_i[1:-2]
    superDiag= x_i[2:-1]

    d = np.zeros(N)
    d[-1] = x_i[-1]

    A = scipy.sparse.diags([mainDiag,subDiag,superDiag],[0,-1,1], shape=(N,N), format='csc')
    return A,d


def solveCoolingRib(N):
    """ Function that calculates the temparature in the cooling rib in problem c in the last theory exercise.
        The function solves the enterier using a sparse solver (use the function 'createMatrix' to get the A matrix
        and the RHS vector d). Be sure to add the temperatures at the boundaries.
        Args:
            N (int): number of unknowns

        Returns:
            x (array): discretized domain. Array with length (N + 2)
            Theta (array): temperature in the cooling rib with. Array with length (N + 2)

    """

    A, d = SytemOfEquations(N)

    ThetaSol = scipy.sparse.linalg.spsolve(A, d)

    h = 1. / (N + 1)
    Beta2 = 4.

    x = np.linspace(0, 1, N + 2)
    theta1 = ThetaSol[0]
    theta0 = theta1 / (1 + (Beta2 / 2) * h + (Beta2 ** 2 / 12) * h ** 2)
    thetaEnd = 1

    Theta = np.append(theta0, ThetaSol)
    Theta = np.append(Theta, thetaEnd)

    return x, Theta

    