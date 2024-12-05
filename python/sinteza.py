import numpy as np
import matplotlib.pyplot as plt
import time


def solve_poly(p0, pT, v0, vT, T):
    A = np.array([
        [T**3, T**2],
        [3*T**2, 2*T]
    ])
    b = np.array([pT - p0 - v0*T, vT - v0]).T
    coefs = np.linalg.inv(A) @ b
    a0 = p0
    a1 = v0
    a2 = coefs[1]
    a3 = coefs[0]
    
    return [a0, a1, a2, a3]

def search_poly(p0, pT, v0, vT, T_start, T_stop, dt, v_max, acc_max):
    
    n_steps = int((T_stop - T_start) / dt)
    T = T_start
    for i in range(1, n_steps):
        T = T_start + i*dt
        coefs = solve_poly(p0, pT, v0, vT, T)
        
        poly = np.polynomial.Polynomial(coefs)
        poly_prim = poly.deriv(1)
        poly_2nd = poly.deriv(2)
        
        t = np.linspace(T_start, T, num=i+2)
        
        v = poly_prim(t)
        a = poly_2nd(t)
        if (np.max(np.abs(v)) <= v_max) and (np.max(np.abs(a)) < acc_max):
            return poly, T
        


if __name__ == "__main__":
    
    
    # data = [0, 1, 2, 3 ,4 ,5, 6, 7, 8, 9, 10]
    # data = np.linspace(start = 0, stop = 2*np.pi, num=100)
    # x = np.array(data, dtype=np.float32)
    # y = np.sin(x)

    # plt.scatter(x,y, c='r', marker='s')
    # plt.show() # blokirajuca funkcija
    
    # Polinomi
    start = time.time()
    poly, T = search_poly(0, 10, 0, 0, 0.5, 30, 0.05, 5, 0.25)
    stop = time.time()
    
    print(f"Potrebno vreme: {stop - start}")
    
    t = np.linspace(0.5, T, num = 100)
    print(T)
    x = t
    y = poly(t)
    poly_prim = poly.deriv(1)
    y_prim = poly_prim(t)
    y_acc = poly.deriv(2)(t)
    
    plt.plot(x,y)
    plt.plot(x,y_prim)
    plt.plot(x,y_acc)
    
    # x = t
    # y = poly(t)
    
    # plt.scatter(x,y)
    plt.show()
