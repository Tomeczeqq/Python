import numpy as np
from scipy.linalg import lu_factor, lu_solve, inv, qr
import time
import matplotlib.pyplot as plt

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
def equations():
    sizes = [10, 30, 50, 70, 90]
    times_lu, times_inv, times_qr = [], [], []
    for n in sizes:
        A, b = generate_system(n)
        start_time = time.time()
        solve_lu(A, b)
        lu_time = time.time() - start_time
        times_lu.append(lu_time)

        start_time2 = time.time()
        solve_inverse(A, b)
        inv_time = time.time() - start_time2
        times_inv.append(inv_time)

        start_time3 = time.time()
        solve_qr(A, b)
        qr_time = time.time() - start_time3
        times_qr.append(qr_time)
    plt.figure()
    plt.plot(sizes, times_lu, label='LU', marker='o')
    plt.plot(sizes, times_inv, label='Odwrocenie macierzy', marker='o')
    plt.plot(sizes, times_qr, label='QR', marker='o')
    plt.xlabel('Rozmiar ukladu rownan (n)')
    plt.ylabel('Czas (s)')
    plt.title('Czas rozwiazania ukladu rownan w zaleznosci od rozmiaru')
    plt.legend()
    plt.grid(True)
    plt.show()

equations()