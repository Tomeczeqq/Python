from math import exp

def e_do_potegi_x(x, liczba_iteracji=100, epsilon=10**-8):
    wynik = 1.0
    silnia = 1.0
    for i in range(1, liczba_iteracji):
        silnia *= i
        wyraz = (x**i) / silnia
        if abs(wyraz) < epsilon:
            break
        wynik += wyraz
    return wynik

xd=[1,5,10,-1,-5,-10]
for x in xd:
    print("Dla x = " + str(x) + " wynik mojego algorytmu wynosi: " + str(e_do_potegi_x(x)) + " wobec wartości z biblioteki: " + str(exp(x)))