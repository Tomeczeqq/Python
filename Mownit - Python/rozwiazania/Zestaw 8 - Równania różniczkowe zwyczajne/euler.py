from math import sin, cos, exp

def function(x: float, y: float) -> float:
    return sin(x) * cos(x) - y * cos(x)

def solution(x: float) -> float:
    return exp(-sin(x)) + sin(x) - 1

def Euler(n: int, h: float, x: float, y: float):
    for _ in range(n):
        m = function(x, y)
        y += h * m
        x += h
    return x, y

x, y, n_values = 0, 0, [10, 100, 1000, 10000, 100000, 1000000]
results = [(n, Euler(n, 5 / n, x, y)[1], solution(5)) for n in n_values]
for n, y_hat, y_real in results:
    print(f"n = {n}, y^ = {y_hat:.14f}, y = {y_real:.14f}, y_delta = {abs(y_hat - y_real):.16f}")