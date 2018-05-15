import numpy as np
import matplotlib.pyplot as plt

def FTCSscheme(Nx,Nt):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter

    A = np.zeros((Nt,Nx))
    r=0.5
    A[:,0] = 0
    A[-1,:] = 0
    A[:,0] = 100
    max = 0
    for i in range(1,Nt):
        for j in range(1,Nx-1):
            A[i,j] = A[i-1,j]*(1-2*r)+ A[i-1,j-1]*r + A[i-1,j+1]*r
            if A[i,j] > max:
                max= A[i,j]
    x = np.linspace(0, 1,Nx)
    t = np.linspace(0,1,Nt)
    fig = plt.figure()
    #for i in A:
    #    plt.plot(x,i)
    #plt.show()
    X,T = np.meshgrid(x,t)
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, T, A, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    Ttop = A[0,0]
    ax.set_zlim(0, Ttop)
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('T [$^o$C]')

    xticks = np.linspace(0.0, 1, 5)
    ax.set_xticks(xticks)
    plt.show()

    yticks = np.linspace(0.0, 1, 5)
    ax.set_yticks(yticks)

FTCSscheme(14,14)




