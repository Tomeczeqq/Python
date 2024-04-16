import numpy as np
from scipy.integrate import quadrature

def f(x):
    return 1/(1+x**2)

def legendreGen(n):
    p = []
    p.append(np.poly1d([1]))
    p.append(np.poly1d([1, 0]))
    x = np.poly1d([1, 0])
    for i in range(1, n):
        p.append((2 * i + 1)/(i + 1) * p[i] * x - (i / (i + 1)) * p[i-1])
    return p

def approxF(n):
    leg = legendreGen(n)
    c = []
    ff = [np.poly1d([0])]
    for i in range(0, n):
        c.append(quadrature((lambda x: f(x) * leg[i](x)), -1,1)[0] / quadrature((lambda x: leg[i](x)**2), -1, 1)[0])
        ff.append(c[i] * leg[i])
    return sum(ff)

def Integr(n):
    i = approxF(n).integ()
    return i(1) - i(-1)

print("Wartosc calki wynosi:")
print(Integr(8))
print("Wartosc bledu bezwzglednego wynosi:")
print(Integr(8) - np.pi/2)