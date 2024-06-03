from math import sin, cos, exp

def function(x: float, y: float) -> float:
    return sin(x) * cos(x) - y * cos(x)

def solution(x: float) -> float:
    return exp(-sin(x)) + sin(x) - 1

def Runge_Kutta(n: int, h: float, x: float, y: float):
    for _ in range(n):
        k1 = h * function(x, y)
        k2 = h * function(x + h / 2, y + k1 / 2)
        k3 = h * function(x + h / 2, y + k2 / 2)
        k4 = h * function(x + h, y + k3)
        x += h
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y

x, y, n_values = 0, 0, [10, 100, 1000, 10000, 100000, 1000000]
results = [(n, Runge_Kutta(n, 5 / n, x, y)[1], solution(5)) for n in n_values]
for n, y_hat, y_real in results:
    print(f"n = {n}, y^ = {y_hat:.14f}, y = {y_real:.14f}, y_delta = {abs(y_hat - y_real):.16f}")