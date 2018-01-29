#Oppgave 1:
from problem1 import function, plotXY, NewtonSol,ExactSol

N = 100;
[Y,X] = function(N)
plotXY(X,Y)
[X_new,Y_new] = NewtonSol(N)
plotXY(X_new,Y_new)
[X_exa,Y_exa] = ExactSol(N)
plotXY(X_exa,Y_exa)