import numpy as np
import math

def f(x):
    return np.exp(-x**2) * np.cos(x)

a = -1000
b = 1000
true_value = math.sqrt(math.pi) / math.pow(math.e, 0.25)

def rectangle():
    print("Wyniki dla metody prostokatow:")
    for steps in [1000, 2000, 4000]:
        h = (b - a) / steps
        xs = np.linspace(a, b, num=steps, endpoint=False)
        Int = sum(f(x) * h for x in xs)
        print("Dla n =", steps, " : ", Int, " blad bezwgledny: ", Int - true_value)

def trapeze():
    print("Wyniki dla metody trapezow:")
    for steps in [1000, 2000, 4000]:
        h = (b - a) / steps
        xs = np.linspace(a, b, num=steps + 1, endpoint=True)
        Int = (f(xs[0]) + f(xs[-1])) / 2 + sum(f(x) for x in xs[1:-1])
        Int *= h
        print("Dla n =", steps, " : ", Int, " blad bezwgledny: ", Int - true_value)

def simpson():
    print("Wyniki dla metody Simpsona:")
    for steps in [1000, 2000, 4000]:
        if steps % 2 != 0:
            steps += 1
        h = (b - a) / steps
        xs = np.linspace(a, b, num=steps + 1)
        Int = f(xs[0]) + f(xs[-1])
        for i in range(1, steps):
            if i % 2 == 0:
                Int += 2 * f(xs[i])
            else:
                Int += 4 * f(xs[i])
        Int *= h / 3
        print("Dla n =", steps, " : ", Int, " blad bezwgledny: ", Int - true_value)

rectangle()
trapeze()
simpson()