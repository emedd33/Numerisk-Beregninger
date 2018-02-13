#Oppgave 1:
from problem1 import function, plotXY, NewtonSol,ExactSol
from problem2 import PendulumEuler
from problem3 import PendulumHeuns, amplitudePeak

N = 100;

def problem1(N):

    [Y, X] = function(N)
    plotXY(X, Y)
    [X_new, Y_new] = NewtonSol(N)
    plotXY(X_new, Y_new)
    [X_exa, Y_exa] = ExactSol(N)
    plotXY(X_exa, Y_exa)

def problem2(N):
    thetta,t,vel = PendulumEuler(N)
    plotXY(t,thetta)

def problem3(N):
    thetta, vel, t = PendulumHeuns(N)
    thetta_amp, t_amp, vel_amp = amplitudePeak(thetta,vel,t,N)
    print(t_amp)
    plotXY(t, thetta)



problem1(N)
problem2(N)
problem3(N)