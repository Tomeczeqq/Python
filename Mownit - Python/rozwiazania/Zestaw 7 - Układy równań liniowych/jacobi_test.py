import numpy as np

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

def calculation(precision: float):
    A = np.array([[10, -1, 2, -3],
                  [1, 10, -1, 2],
                  [2, 3, 20, -4],
                  [3, 2, 1, 20]])
    b = np.array([0, 5, -10, 15]).reshape(-1, 1)
    solves, results = jacobi_iteration(A, b, precision)
    print("Dla precyzji:", precision, "mamy:", len(results), "iteracji")

calculation(1e-3)
calculation(1e-4)
calculation(1e-5)