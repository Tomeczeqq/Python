import numpy as np
from numpy.polynomial.hermite import hermgauss

def f(x):
    return np.exp(-x ** 2) * np.cos(x)

nodes, weights = hermgauss(30)
print("Wynik metody całkowania przy pomocy kwadratury Gaussa-Hermite'a:")
print(np.sum(weights * f(nodes)))