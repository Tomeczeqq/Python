import numpy as np
from scipy.linalg import lu_factor, lu_solve, inv, qr
import time

def generate_system(n):
    A = np.random.randn(n, n)
    b = np.random.randn(n)
    return A, b

def solve_lu(A, b):
    lu, piv = lu_factor(A)
    x = lu_solve((lu, piv), b)
    return x

def solve_inverse(A, b):
    A_inv = inv(A)
    x = np.dot(A_inv, b)
    return x

def solve_qr(A, b):
    Q, R = qr(A)
    y = np.dot(Q.T, b)
    x = np.linalg.solve(R, y)
    return x

def check_solution(A, x, b):
    result = np.dot(A, x)
    return np.allclose(result, b)

def equations(n):
    A, b = generate_system(n)
    start_time = time.time()
    x_lu = solve_lu(A, b)
    lu_time = time.time() - start_time
    start_time2 = time.time()
    x_inv = solve_inverse(A, b)
    inv_time = time.time() - start_time2
    start_time3 = time.time()
    x_qr = solve_qr(A, b)
    qr_time = time.time() - start_time3
    print(f"n jest równe {n}")
    print(f"Czas rozwiazania metoda LU: {lu_time:.8f} s")
    print(f"Czas rozwiazania metoda odwrocenia macierzy: {inv_time:.8f} s")
    print(f"Czas rozwiazania metoda QR: {qr_time:.8f} s")

    lu_correct = check_solution(A, x_lu, b)
    inv_correct = check_solution(A, x_inv, b)
    qr_correct = check_solution(A, x_qr, b)
    print(f"Rozwiazanie metoda LU jest poprawne: {lu_correct}")
    print(f"Rozwiazanie metoda odwrocenia macierzy jest poprawne: {inv_correct}")
    print(f"Rozwiazanie metoda QR jest poprawne: {qr_correct}")

equations(75)