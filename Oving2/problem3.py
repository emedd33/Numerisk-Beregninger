
import numpy as np
def PendulumHeuns(N):
    h = 10 / N
    vel = [0]
    velp = [0]
    t = [0]
    thetta = [85]
    thettap = [85]
    for i in range(N):
        thettap_app = np.radians(thetta[i])+h*func2(vel[i])
        thettap.append(np.degrees(thettap_app))

        velp_app = vel[i] + h*func1(vel[i],thetta[i])
        velp.append(velp_app)

        thetta_app = np.radians(thetta[i]) + h/2*(func2(vel[i])+func2(velp[i]))
        thetta.append(np.degrees(thetta_app))

        vel_app = vel[i] + h/2*(func1(vel[i],thetta[i])+func1(velp[i],thettap[i]))
        vel.append(vel_app)

        t.append(t[i] + h)
    return thetta, vel,t

def func1(vel,thetta):
    my = 1
    m = 1
    g = 9.81
    l = 1

    res = -1*(my/m*vel+g/l*np.sin(np.radians(thetta)))
    return res

def func2(vel):
    return vel

def amplitudePeak(thetta,vel,t,N):
    t_amp = []
    Y_amp = []
    thetta_amp = []
    for i in range(N):
        if(i != 0 and i!= N):
            if(np.abs(thetta[i])>np.abs(thetta[i-1])):
                if (np.abs(thetta[i])> np.abs(thetta[i+1])):
                    t_amp.append(t[i])
                    Y_amp.append(vel[i])
                    thetta_amp.append(thetta[i])
    return thetta_amp,t_amp,Y_amp


