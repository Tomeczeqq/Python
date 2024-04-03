''' Tomasz Janeczko 414613
Dane wejsciowe: slowo s skladajace sie wylacznie z malych liter alfabetu lacinskiego
Szukane: dlugosc najdluzszego palindromu nieparzystej dlugosci
Opis rozwiazania:
Dla kazdej litery na indeksach [1,n-2] ustalam, ze sa one srodkiem mojego liczenego palindroma. Nastepnie tak dlugo jak sie
zgadzaja litery na odpowiednich indeksach to licze dlugosc takiego palindromu. W przypadku kiedy liczenie palindromu zatrzymuje
sie ze wzgledu na konce przedzialow uwzgledniam, ze sa tam dwie opcje (ostatnie porownanie znakow sie 'zgadza' lub tez nie).
Poprawność rozwiazania:
Moje rozwiazanie jest poprawne, poniewaz sprawdzam kazda mozliwa opcje i dla niej licze wynik. Ze wszystkich uzyskanych takich
wynikow biore najwiekszy i jest to dlugosc najdluzszego palindromu o nieparzystej dlugosci.
Szacowana złożoność obliczeniowa:
Zlozonosc obliczeniowa szacuje na O(n^2), poniewaz wykonuje dwie petle (jedna w drugiej) po calej dlugosci napisu s'''
from zad1testy import runtests

def ceasar(s):
    n=len(s)
    wynik=1
    for i in range(1,n-1):
        j,k=i-1,i+1
        while s[j]==s[k] and j>0 and k<n-1:
            j-=1
            k+=1
        if (j==0 or k==n-1) and s[j]==s[k]:
            wynik=max(wynik,k-j+1)
        wynik=max(wynik,k-j-1)
    return wynik

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ceasar,all_tests=True)