from typing import Callable
from random import uniform
from math import sqrt, pi

def function1(x: float) -> float:
    return x ** 2 + x + 1

def function2(x: float) -> float:
    return sqrt(1 - x ** 2)

def function3(x: float) -> float:
    return 1 / sqrt(x)

def rectangle_method(a: float, b: float, eps: float, fun: Callable[[float], float]) -> float:
    n = int((b - a) / eps)
    integral = 0.0
    for i in range(n):
        x = a + i * eps
        integral += fun(x) * eps
    return integral

a, b, epsilons = 0, 1, [1e-3, 1e-4, 1e-5, 1e-6]
for e in epsilons:
    print("For epsilon =", e)
    result1 = rectangle_method(a, b, e, function1)
    result2 = rectangle_method(a, b, e, function2)
    result3 = rectangle_method(1e-8, b, e, function3)
    print("Result for function1:", result1)
    print("Result for function2:", result2)
    print("Result for function3:", result3)