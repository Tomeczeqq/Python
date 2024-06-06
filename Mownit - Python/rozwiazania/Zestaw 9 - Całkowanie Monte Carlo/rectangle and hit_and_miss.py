import time
import matplotlib.pyplot as plt
from typing import Callable
from random import uniform
from math import sqrt

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

def hit_and_miss(a: float, b: float, n: int, h: float, function: Callable[[float], float]) -> float:
    S = 0
    for i in range(n):
        x = uniform(a, b)
        y = uniform(0, h)
        if y < function(x):
            S += 1
    return ((b - a) * h) * S / n

a, b, epsilons = 0, 1, [1e-3, 1e-4, 1e-5, 1e-6]
h_values = [function1(1), function2(0), function3(1e-8)]
rectangle_times, monte_carlo_times = [], []
for e in epsilons:
    n_monte_carlo = int(1 / e)
    print(f"For n = {n_monte_carlo} and for epsilon = {e}")
    start_time = time.time()
    result1 = rectangle_method(a, b, e, function1)
    result2 = rectangle_method(a, b, e, function2)
    result3 = rectangle_method(1e-8, b, e, function3)
    end_time = time.time()
    rectangle_times.append(end_time - start_time)
    print(f"Rectangle Method: {end_time - start_time} seconds")
    start_time = time.time()
    result1_mc = hit_and_miss(a, b, n_monte_carlo, h_values[0], function1)
    result2_mc = hit_and_miss(a, b, n_monte_carlo, h_values[1], function2)
    result3_mc = hit_and_miss(1e-8, b, n_monte_carlo, h_values[2], function3)
    end_time = time.time()
    monte_carlo_times.append(end_time - start_time)
    print(f"Monte Carlo Method: {end_time - start_time} seconds")

plt.plot(epsilons, rectangle_times, label='Rectangle Method')
plt.plot(epsilons, monte_carlo_times, label='Monte Carlo Method')
plt.xlabel('Epsilon')
plt.ylabel('Computation Time (s)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.title('Comparison of Integration Methods')
plt.show()