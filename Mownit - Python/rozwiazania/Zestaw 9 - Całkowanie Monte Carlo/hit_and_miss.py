from typing import Callable
from random import uniform
from math import sqrt, pi


def function1(x: float) -> float:
    return x ** 2 + x + 1

def function2(x: float) -> float:
    return sqrt(1 - x ** 2)

def function3(x: float) -> float:
    return 1 / sqrt(x)

def hit_and_miss(a: float, b: float, n: int, h: float, function: Callable[[float], float]) -> float:
    S: int = 0
    for i in range(n):
        x = uniform(a, b)
        y = uniform(0, h)
        if y < function(x):
            S += 1
    return ((b - a) * h) * S / n

a, b, sample_sizes = 0, 1, [10, 100, 1000, 10000, 100000]
exact1, exact2, exact3 = 11/6, pi/4, 2

for n in sample_sizes:
    print("For n =", n)
    result1 = hit_and_miss(a, b, n, function1(1), function1)
    result2 = hit_and_miss(a, b, n, function2(0), function2)
    result3 = hit_and_miss(a, b, n, function3(1e-8), function3)
    print("Result for function1:", result1, "Error for function1:", abs(result1 - exact1))
    print("Result for function2:", result2, "Error for function2:", abs(result2 - exact2))
    print("Result for function3:", result3, "Error for function3:", abs(result3 - exact3))