#Liczenie piewiastkow trojmianu kwadratowego
from math import sqrt #konkretne funkcje
#from math import* - wszystkie funkcje (NIEZALECANE)
#import math - trzeba pisac math.sqrt(delta)
#import math as m - trzeba pisac m.sqrt(delta)
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
delta=b*b-4*a*c
if delta>=0:
    pierw=sqrt(delta)
    res1=(-b-pierw)/(2*a)
    res2=(-b+pierw)/(2*a)
    print("Pierwiastkami są: ",res1," ",res2)
else:
    print("Brak pierwiastkow")
