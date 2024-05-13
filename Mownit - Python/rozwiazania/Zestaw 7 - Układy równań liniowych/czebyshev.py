from random import randint
import numpy as np

n = 5
def generate_matrixs():
    A = [[0.0 for _ in range(n)] for _ in range(n)]
    X = [randint(0, 1) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                if i == 0 or i == n - 1:
                    A[i][j] = 1
                else:
                    A[i][j] = 2
            elif i == j + 1:
                A[i][j] = 1 / (i + 1)
            elif j == i + 1:
                A[i][j] = 1 / (i + 2)
    return A, X

def chebyshev_iteration(A: np.array, b: np.array, precision: float):
    x = np.zeros((len(A[0]), 1))
    eigs = np.linalg.eig(A)[0]
    min_eig, max_eig = np.min(np.abs(eigs)), np.max(np.abs(eigs))
    r = b - A @ x
    x_new = x + 2 * r / (min_eig + max_eig)
    r = b - A @ x_new
    t = [1, -(min_eig + max_eig) / (max_eig - min_eig)]
    results = []
    beta = -4 / (max_eig - min_eig)
    norm_b = np.linalg.norm(b)
    norm_one, norm_two = 2, 2
    iteration = 1
    while norm_one > precision or norm_two > precision:
        norm_one = np.linalg.norm(abs(x_new - x))
        norm_two = np.linalg.norm(A @ x_new - b) / norm_b
        results.append((iteration, norm_one, norm_two))
        iteration += 1
        t.append(2 * t[1] * t[-1] - t[-2])
        alpha = t[-3] / t[-1]
        old_x, old_x_new = x, x_new
        x = old_x_new
        x_new = (1 + alpha) * old_x_new - alpha * old_x + (beta * t[-2] / t[-1]) * r
        r = b - A @ x_new
    return x_new, results


def calculation():
    matrixA, matrixX = generate_matrixs()
    A = np.array(matrixA)
    x = np.array(matrixX).reshape(-1, 1)
    b = A @ x
    solutions, results = chebyshev_iteration(A, b, 1e-6)
    print("Macierz A:")
    print(A)
    print("Wektor b:")
    print(b)
    print("Wektor x z rozwiązaniem:")
    print(solutions)
    print("Wyniki iteracji metody Czebyszewa:")
    for res in results:
        print("Numer iteracji:", res[0], "norma residuum:", res[1], "norma błędu residuum:", res[2])

calculation()