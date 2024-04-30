def f(x):
    return x ** 3 - 5 * x - 6
def df(x):
    return 3 * x ** 2 - 5
def newton_raphson(f, df, x0, tolerance=1e-8, max_iter=10):
    x_n = x0
    for i in range(max_iter):
        x_next = x_n - f(x_n) / df(x_n)
        print(f"Iteracja {i + 1}: x_n = {x_n:.8f}, x_next = {x_next:.8f}")
        if abs(x_next - x_n) < tolerance:
            return x_next
        x_n = x_next
    raise ValueError("Metoda Newtona-Raphsona nie zbiega w podanym zakresie")

try:
    solution = newton_raphson(f, df, 2.5)
    print(f"Rozwiązanie równania x^3 - 5x - 6 = 0 w przedziale [2, 3] jest równe x = {solution:.8f}")
except ValueError as e:
    print(str(e))