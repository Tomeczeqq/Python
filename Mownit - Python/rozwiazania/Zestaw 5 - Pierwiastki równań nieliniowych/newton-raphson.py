import numpy as np

def F(x):
    x1, x2 = x
    return np.array([x1 ** 2 + x1 * x2 ** 3 - 9, 3 * x1 ** 2 * x2 - x2 ** 3 - 4])
def J(x):
    x1, x2 = x
    return np.array([[2 * x1 + x2 ** 3, 3 * x1 * x2 ** 2], [6 * x1 * x2, 3 * x1 ** 2 - 3 * x2 ** 2]])
def newton_raphson(F, J, x0, tolerance=1e-8, max_iter=10):
    x_n = np.array(x0)
    for i in range(max_iter):
        F_x = F(x_n)
        J_x = J(x_n)
        delta_x = np.linalg.solve(J_x, F_x)
        x_next = x_n - delta_x
        print(f"Iteracja {i + 1}: x_n = {x_n}, x_next = {x_next}")
        if np.linalg.norm(delta_x) < tolerance:
            return x_next
        x_n = x_next
    raise ValueError("Metoda Newtona-Raphsona nie zbiega w podanym zakresie")

try:
    solution = newton_raphson(F, J, [1, 1])
    print(f"Rozwiazanie ukladu rownan x^2 + x^2^3 = 9 oraz 3x^2x - x^2^3 = 4 to x1 = {solution[0]:.8f} i x2 = {solution[1]:.8f}")
except ValueError as e:
    print(str(e))