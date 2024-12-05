# u terminalu: pip install matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np


def sinteza_polinomom(p0, pT, v0, vT, v_max)->tuple:
    """Sinteza trajektorije polinomom treceg reda. Za pocetne uslove koji su dati.
    Ova funkcija vraca parametre polinoma u vidu tupla.

    Args:
        p0 (float): Pocetna pozicija
        pT (float): Krajnja pozicija
        v0 (float): Pocetna brzina
        vT (float): Krajnja brzina
    """
    T_start = 0.1
    T_stop = 20
    dt = 0.01
    t_array = np.linspace(start = T_start,  stop = T_stop, num=int((T_stop-T_start)/dt))
    for T in t_array:
        A = np.array([
            [T**3, T**2],
            [3*T**2, 2*T]
        ])
        
        B = np.array([pT-p0 - v0*T, vT - v0]).T
        coefs = np.linalg.inv(A) @ B
        
        a0 = p0
        a1 = v0
        a2 = coefs[1]
        a3 = coefs[0]
        
        p = np.polynomial.Polynomial([a0, a1, a2, a3])
        p_prim = p.deriv(1)
        t_tmp = np.linspace(start = 0, stop=T, num=int(T/dt))
        if np.max(abs(p_prim(t_tmp))) <= abs(v_max):
            return a3, a2, a1, a0, T
    return 0, 0, 0, 0, 0

def polinom(a3, a2, a1, a0, t):
    return a3 * t**3 + a2 * t**2 + a1 * t + a0

def polinom_prim(a3, a2, a1, t):
    return 3*a3*t**2 + 2*a2*t + a1

if __name__ == "__main__":
    
    # x = [2, 3 , 5, 6, 7, 8, 9, 10]
    # y = [math.sin(data) for data in x] # za svaki 'i' u 'x' dodaj na listu sin(i)
    
    # # ovo je duzi nacin
    # # y = []
    # # for data in x:
    # #     y.append(data)
    
    # plt.scatter(x, y, c='r', marker='*') # tackasto plotovanje
    # plt.plot(x, y, c='g') # linijsko (c = color)
    # plt.show() # blokirajuca funkcija

    dt = 0.01
    a3, a2, a1, a0, vreme = sinteza_polinomom(5, 14, 1, 0, v_max=1)
    print("Potrebno vreme da se izvrsi: ", vreme)
    
    t_array = np.linspace(start = 0.1, stop=vreme, num=int((vreme - 0.1)/dt))
    
    poly = np.polynomial.Polynomial([a0, a1, a2, a3])
    poly_prim = poly.deriv(1)
    
    plt.plot(t_array, poly(t_array))
    plt.plot(t_array, poly_prim(t_array))
    
    plt.show()
