import numpy as np

p = [np.poly1d([1]), np.poly1d([1, 0])]
x = np.poly1d([1, 0])
for i in range(1, 6):
    p.append((2*i+1)/(i+1)*p[i]*x-(i/(i+1))*p[i-1])
    print(p[i+1])

