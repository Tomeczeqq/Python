''' Tomasz Janeczko 414613
Dane wejsciowe: tablica T zawierajaca n napisow (z malych liter alfabetu lacinskiego) o lacznej dlugosci N
Szukane: sila najsilniejszego napisu z tablicy T
Opis rozwiazania:
Najpierw kazdy napis w tablicy T ustawiamy tak, aby z dwoch opcji (od przodu lub od tylu) byl w T ten pierwszy leksykograficznie.
Nastepnie sortujemy cala tablice leksykograficznie quicksortem z usunieta rekurencja ogonowa. Teraz jedynie pozostaje nam zliczyc wynik
wedlug schematu: jesli poprzedni napis jest ten sam to temp+=1, w przeciwnym wypadku temp=1
Poprawność rozwiazania:
Rozwiazanie jest poprawne, poniewaz dzieki funckji leks i algorytmowi quicksort wiemy, ze kazde dwa rownowazne napisy znajda sie kolo
napisu rownowaznego dla nich samych w tablicy T. Majac taka tablice T latwo mozemy odczytac juz wynik.
Szacowana złożoność obliczeniowa:
Szacuje moja zlozonosc na O(N+nlogn), poniewaz korzystam z algorytmu quicksort o zlozonosci O(nlogn) oraz jednoczesnie musze przejsc
iles razy po dlugosci wszystkich napisow - np w funkcji leks (co ma zlozonosc O(N)), dlatego calosc ma zlozonosc O(N+nlogn).'''
from zad3testy import runtests

def leks(x,y):
    n=len(x)
    for i in range(n):
        if ord(x[i])<ord(y[i]):
            return x
        elif ord(x[i])>ord(y[i]):
            return y
    return x

def partition(T,l,r):
    if l>=r:
        return l
    pivot=T[r]
    j=l
    for i in range(l,r):
        if T[i]<pivot:
            T[i],T[j]=T[j],T[i]
            j+=1
    T[r],T[j]=T[j],T[r]
    return j

def quicksort(T,l,r):
    while l<r:
        q=partition(T,l,r)
        quicksort(T,l,q-1)
        l=q+1

def strong_string(T):
    n=len(T)
    #Porzadek leksykograficzny kazdego z napisow - z przodu czy z tylu
    for i in range(n):
        T[i]=(leks(T[i],T[i][::-1]))
    quicksort(T,0,n-1)
    temp,wynik=1,1
    for i in range(1,n):
        if len(T[i])!=len(T[i-1]) or T[i]!=T[i-1]:
            wynik=max(wynik,temp)
            temp=1
        else:
            temp+=1
    return wynik

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string,all_tests=True)