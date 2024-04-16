import numpy as np
from math import log

def f(x):
    return 1 / (x+1)

def rectangle():
    print("Wyniki dla metody prostokatow:")
    for steps in [1, 3, 5]:
        length = 1
        xs = np.linspace(0, length, num=steps+1, endpoint=False)
        Int = sum(map(lambda x: f(x) * length / steps, xs[1::]))
        print("Dla n =", steps, " : ", Int, " blad bezwgledny: ", Int - log(2))

def trapeze():
    print("Wyniki dla metody trapezow:")
    for steps in [2, 3, 5]:
        length = 1
        h = length / (steps - 1)
        xs = np.linspace(0, length, num=steps, endpoint=True)
        Int = sum(map(lambda x: (f(x) + f(x-h)) * h / 2, xs[1::]))
        print("Dla n =", steps, " : ", Int, " blad bezwgledny: ", Int - log(2))

def simpson():
    print("Wyniki dla metody Simpsona:")
    for steps in [3, 5]:
        length = 1
        h = length / (steps - 1)
        xs = np.linspace(0, length, num=int(steps/2)+1, endpoint=True)
        Int = sum(map(lambda x: (f(x) + 4*f(x-h) + f(x-2*h)) * h/3, xs[1::]))
        print("Dla n =", steps, " : ", Int, " blad bezwgledny: ", Int - log(2))

rectangle()
trapeze()
simpson()