import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def equations(t, Y):
    y1, y2 = Y
    dy1dt = y2
    dy2dt = t - y1
    return [dy1dt, dy2dt]


def shooting_method(y0, y_target, x_target, initial_guess, tol=1e-7, max_iter=1000):
    def boundary_residual(z0):
        sol = solve_ivp(equations, [0, x_target], [y0, z0], t_eval=[x_target])
        y1_final = sol.y[0][-1]
        return y1_final - y_target
    z0 = initial_guess
    for _ in range(max_iter):
        res = boundary_residual(z0)
        if abs(res) < tol:
            print("Metoda strzalow zbiega do oczekiwanego wyniku")
            return solve_ivp(equations, [0, x_target], [y0, z0], t_eval=np.linspace(0, x_target, 100))
        z0 -= res / y_target
    print("Metoda strzalow nie zbiega do oczekiwanego wyniku")
    return solve_ivp(equations, [0, x_target], [y0, z0], t_eval=np.linspace(0, x_target, 100))

y0, y_target, x_target, y_ = 1, np.pi / 2 - 1, np.pi / 2, 0.5
sol = shooting_method(y0, y_target, x_target, y_)
x_vals = np.linspace(0, np.pi/2, 100)
y_exact = np.cos(x_vals) - np.sin(x_vals) + x_vals
plt.plot(sol.t, sol.y[0], 'b', label='Metoda strzalow')
plt.plot(x_vals, y_exact, 'r--', label='Dokladne rozwiazanie')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.title('Rozwiazanie rownania rozniczkowego metoda strzalow')
plt.show()