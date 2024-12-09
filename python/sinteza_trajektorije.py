import numpy as np
import matplotlib.pyplot as plt
import time


def sinteza_trajektorije(p0, pT, v0, vT, T_start, v_max, max_steps):
    
    a0 = p0
    a1 = v0
    
    dt = 0.01
    for i in range(max_steps):
        
        T = T_start + i * dt
        A = np.array(
            [
                [T**3, T**2],
                [3*T**2, 2*T]
            ]
        )
        
        b = np.array([
            pT - a0 - a1 * T,
            vT - a1
        ]).T
        
        x = np.linalg.inv(A) @ b
        
        a2 = x[1]
        a3 = x[0]
        
        coefs = [a0, a1, a2, a3]
        vremena = np.linspace(0, T, 1000)
        brzine = calculate_polynomial(coefs, vremena, first_derivative=True)
        
        if np.max(np.abs(brzine)) < v_max:
            
            return coefs, T

        
    return [0, 0, 0, 0], T_start

def calculate_polynomial(coefs : list, t, first_derivative = False):
    """Ovo je funkcija za racunanje vrednosti polinoma u datim vremenskim trenucima

    Args:
        coefs (list): koeficijenti polinoma, od [a0, a1, ... an]
        t (float | np.array): vremenski trenuci za racunanje polinoma 

    Returns:
        (float | list | np.array): vrednosti polinoma u datim trenucima
    """
    stepen_polinoma = len(coefs) - 1
    if first_derivative:
        coefs = coefs[1:]
        
    ret = 0
    for i, a in enumerate(coefs):
        tmp = a * pow(t,i)
        if first_derivative:
            tmp = tmp * (i + 1)
        ret += tmp
    return ret

if __name__ == "__main__":
    
    print()
    print("*"*50)
    print("Sinteza trajektorije")
    print("*"*50, "\n")
    
    start = time.time()
    coefs, T = sinteza_trajektorije(0, 0.2, 0, 0, 0.1, 1, 1000)
    end = time.time()
    
    print(f"Potrebno vreme za sintezu: {end-start}s")
    
    x_values = np.linspace(start=0, stop=T, num=100)
    
    polinom = np.polynomial.Polynomial(coefs)
    poli_prim = polinom.deriv(1)
    poli_snd = polinom.deriv(2)  
    # y_values = calculate_polynomial(coefs, x_values)
    # y_values_2 = calculate_polynomial(coefs, x_values, first_derivative=True)
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.scatter(x_values, polinom(x_values), c="r")
    ax2.scatter(x_values, poli_prim(x_values), c="g")
    ax3.scatter(x_values, poli_snd(x_values), c="b")
    plt.show()
    
  
    
