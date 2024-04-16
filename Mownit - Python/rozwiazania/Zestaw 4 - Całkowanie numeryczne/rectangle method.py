import numpy as np

def f(x):
    return 1 / (1+x**2)

def rectangle():
    print("Wynik dla metody prostokatow:")
    length = 1.0
    h = 0.1
    xs = np.linspace(0, length, num=10, endpoint=False)
    Int = sum(map(lambda x: f(x) * h, xs[1::]))
    print("Dla I = ", Int)

rectangle()