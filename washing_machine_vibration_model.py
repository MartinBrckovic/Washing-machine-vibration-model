# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

#Case paramaters
M = 80
m = 20
l = 0.2
omega = 11
c = 20
k = 50


V = np.array([])
for i in range(0,omega):
    omega = i
    def F1(t):
        return m*l*omega**2*np.sin(omega*t)

#Model solution
    def dYdt(Y, t):
        return np.array([Y[1],
                     (1/(M+m))*(F1(t)-c*Y[1]-k*Y[0])])

#Numerical mesh
    tstart = 0
    tstop = 60
    nt = 1000
    T = np.linspace(tstart, tstop, nt)

#Initial conditions
    Y0 = np.zeros(2)

#Model solving
    Y = odeint(dYdt, Y0, T)
    maxa=np.max(Y[:,0])
    V = np.append(V,maxa)
    print(maxa)

#Response diagram
fig1 = plt.figure()
plt.plot(T, Y[:,0], 'g', label='M+m')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.grid()
plt.show()

#Mass eccentricety diagram
def x_circ(t):
    return l*np.cos(omega*t)
def y_circ(t):
    return l*np.sin(omega*t)

def x_sq(t):
    return 0
def y_sq(i):
    return Y[i,0]

fig2 = plt.figure()
plt.plot(x_circ(T), y_circ(T), "r", label="m")
plt.legend()
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.grid()
plt.show()

def square1(t):
    return np.array([x_sq(t), y_sq(t)])

def circle(t):
    return np.array([x_circ(t), y_circ(t)])

#Animation
fig, ax = plt.subplots()
ax.axis([-4,4,-4,4])
ax.set_aspect("equal")
square, = ax.plot(0, 0, 'gs', ms=55, label='M')
point, = ax.plot(0,l, marker="o", label="m")

def update(i):
    #t = T[i]
    x_s,y_s = square1(i)
    x1 = x_s
    y1 = y_s
    square.set_data(x1,y1)
    
    t = T[i]
    x_c,y_c = circle(t)
    x2 = x_c
    y2 = y_c + Y[i,0]
    point.set_data(x2,y2)
    return point, square,


ani = FuncAnimation(fig, update, frames=np.size(T))
plt.grid()
plt.show()
    
    
    
    
    
    
    
    
    



    
   


    
    
    
    
    
    
