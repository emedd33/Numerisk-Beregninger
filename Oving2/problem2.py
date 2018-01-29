import numpy as np

def PendulumEuler(N):
    my = 1
    m = 1
    g = 9.81
    l = 1
    thetta = [85]
    t = [0]
    vel = [0]
    h = 10/N
    for i in range(N):
        v_app = vel[i] -h*(my/m*vel[i]+g/l*np.sin(np.radians(thetta[i])))
        vel.append(v_app)

        thetta_app = np.radians(thetta[i]) + h*vel[i]
        thetta.append(np.degrees(thetta_app))

        t.append(t[i]+ h)
    return thetta,t,vel


