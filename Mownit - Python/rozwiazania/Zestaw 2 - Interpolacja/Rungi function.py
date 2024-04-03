import numpy as np
import matplotlib.pyplot as s_plt
import scipy.interpolate as inter

d = np.linspace(-1, 1, num=1000, dtype=float)

def f(x):
    return 1 / (1 + 25*(x**2))  #Definicja funkcji interpretowanej

for n in range(4, 10):
    knots = np.linspace(-1, 1, num=n, dtype=float)
    f_int = inter.KroghInterpolator(knots, f(knots)) #Interpolacja funkcji wielomianem
    s_plt.plot(d, f_int(d))
    s_plt.plot(d, f(d))
    s_plt.show()