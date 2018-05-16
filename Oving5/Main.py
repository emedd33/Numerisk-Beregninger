import numpy as np
import scipy
import scipy.sparse
import scipy.sparse.linalg
import matplotlib.pylab as plt
import time
from math import sinh

xmax = 1
ymax = 1
ymin = 0
xmin = 0

N = 10






def SurfacePlot(T,xmin,xmax,ymin,ymax,N,nxTicks=4, nyTicks=4):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter
    x = np.linspace(xmin,xmax,N)
    y = np.linspace(ymin,ymax,N)

    X,Y = np.meshgrid(x,y)

    Ttop = ymax
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, T, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(0, Ttop)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('T [$^o$C]')

    xticks = np.linspace(0.0, xmax, nxTicks + 1)
    ax.set_xticks(xticks)

    yticks = np.linspace(0.0, ymax, nyTicks + 1)
    ax.set_yticks(yticks)


def createMatrix(Nx,Ny):
    T = np.zeros((Ny,Nx))
    T[0, :] = 30
    T[:,0]= 10
    T[:,-1] = 10
    T[0,0] = 20
    T[0,-1] = 20
    nx = Nx-2
    ny = Ny-1
    n = nx*ny
    A = np.zeros((ny,nx))
    mainDiag = np.linspace(-4,-4,n)
    subDiag = np.ones(n-1)
    subDiag[nx-1::nx] = 0
    superDiag = subDiag.copy()

    subDiagN = np.ones(n-nx)
    superDiagN = subDiagN.copy()
    subDiagN[-nx:] = 2
    d= np.ones(n)
    d[0::nx] = -10
    d[0] = -40
    d[1:nx-1] = -30
    d[nx::nx] = -10

    A = scipy.sparse.diags([mainDiag,subDiag,superDiag,subDiagN,superDiagN],[0,-1,1,-nx,nx])
    print(A.toarray())
    return A,d,T


    #starting wth ghost node

    return A
Nx =10
Ny = 10
A,d,T = createMatrix(Nx,Ny)
Temp = scipy.sparse.linalg.spsolve(A,d)
k=1
i=1
print(Temp)
for temp in Temp:
    if k>=(Nx-1):
        k=1
        i+=1
    T[i,k] = temp
    k+=1

SurfacePlot(T,0,1,0,30,Nx)
print(T)
plt.show()
