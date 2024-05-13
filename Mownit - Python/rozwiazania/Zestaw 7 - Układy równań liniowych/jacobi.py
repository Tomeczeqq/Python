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

def jacobi_iteration(A: np.array, b: np.array, precision: float):
    x = np.zeros(len(A[0])).reshape(-1, 1)
    diagonal, remaining = np.diag(A).reshape(-1, 1), A - np.diagflat(np.diag(A))
    results = []
    norm_b = np.linalg.norm(b)
    norm_one, norm_two = 2, 2
    i = 1
    while norm_one > precision or norm_two > precision:
        next_x = (b - remaining @ x) / diagonal
        norm_one = np.linalg.norm(abs(x - next_x))
        norm_two = np.linalg.norm(A @ x - b) / norm_b
        results.append((i, norm_one, norm_two))
        x = next_x
        i += 1
    return x, results

def calculation():
    matrixA, matrixX = generate_matrixs()
    A = np.array(matrixA)
    x = np.array(matrixX).reshape(-1, 1)
    b = A @ x
    solutions, results = jacobi_iteration(A, b, 1e-6)
    print("Macierz A:")
    print(A)
    print("Wektor b:")
    print(b)
    print("Wektor x:")
    print(solutions)
    print("Wyniki iteracji metody Jacobiego:")
    for res in results:
        print("Numer iteracji:", res[0], "norma residuum:", res[1], "norma błędu residuum:", res[2])

calculation()