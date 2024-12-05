import numpy as np
import matplotlib.pyplot as plt
import time

def get_poly(a0, a1, a2, a3, a4, a5, t):
    return a5 * t**5 + a4 * t**4 + a3 * t**3 + a2 * t**2 + a1*t + a0

def get_poly_prim(a1, a2, a3, a4, a5, t):
    return 5*a5 * t**4 + 4*a4 * t**3 + 3*a3 * t**2 + 2 * a2 * t + a1

def get_poly_second(a2, a3, a4, a5, t):
    return 20*a5 * t**3 + 12*a4 * t**2 + 6*a3 * t + 2 * a2


def solve_poly(p0, pT, v0, vT, acc0, accT, T, v_max, a_max):
    
    A = np.array([
        [  T**3,   T**4,   T**5],
        [3*T**2, 4*T**3, 5*T**4],
        [6*T   ,12*T**2,20*T**3]
    ])
    
    b = np.array([
        pT - p0 - v0*T -0.5 * acc0 * T**2,
        vT - v0 - acc0*T,
        accT - acc0
    ])
    
    coefs = np.linalg.solve(A,b)
    a3, a4, a5 = coefs
    a0 = p0
    a1 = v0
    a2 = acc0
    return [a0, a1, a2, a3, a4, a5]
    
    
    

def main():
    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle('Vertically stacked subplots')
    
    t_end = 2
    coefs = solve_poly(0, 5, 0, 0, 0, 0, t_end, 0, 0)
    t = np.linspace(0, t_end, num=100)
    pos = get_poly(*coefs, t=t)
    vel = get_poly_prim(*coefs[1:], t=t)
    acc = get_poly_second(*coefs[2:], t=t)
    
    
    ax1.plot(t, pos) # pos
    ax2.plot(t, vel) # vel
    ax3.plot(t, acc) # acc
    
    plt.show()
    

if __name__ == "__main__":
    
    main()
