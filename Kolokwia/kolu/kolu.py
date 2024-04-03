''' Tomasz Janeczko 414613
Dane wejsciowe: tablica T o rozmiarze n zawierajaca liczby naturalne
Szukane: maksymalna mozliwa ilosc lodow do zjedzenia
Opis rozwiazania:
Na poczatku stworzymy kopiec z elementow z tablicy T. Zwrocmy uwage na to, ze istotny dla nas jest zysk przez wziecie danego elementu do
naszego rozwiazania. Ten zysk jest rowny wartosci tego elementu minus ilosci wszystkich wczesniejszych wzietych elementow (przez zjawisko
topnienia lodow i wybor kolejnego zmniejszaja nam sie wartosci lodow w momencie ich wziecia). Do naszego wyniku bierzemy elementy tak
dlugo, jak uzyskany z nich zysk jest dodatni. Zauwazmy, ze w trakcie sortowania kopcowego,z ktorego korzystamy, zawsze na gorze jest
najwieksza wartosc, ktorej jeszcze nie przejrzelismy, co jest dla nas bardzo korzystne, poniewaz dzieki temu mozemy wykorzystac
optymalizacje, ktora opiera sie na tym ze nie bedziemy sortowac najmniejszych elementow w kopcu (nie jest to przydatne), tylko bierzemy
najwiekszy (chwilowy) element i sprawdzamy czy zysk z niego jest dodatni. Jesli nie, to mozemy zakonczyc przegladanie naszego kopca,
poniewaz kazdy kolejny element jest niewiekszy od tego, ktory zysk jest niedodatni, wiec on tez bedzie niedodatni.
Poprawność rozwiazania:
Mozemy posortowac tablice S nie zwracajac uwage na indeksy. Rozwiazanie jest poprawne, poniewaz zawsze bierzemy element, ktory ma
dodatni zysk (mimo, ze inne elementy straca w tym czasie po 1 snieg, to i tak oplaca nam sie go wziac).
Szacowana złożoność obliczeniowa:
Szacuje moja zlozonosc obliczeniowa na O(nlogn), poniewaz korzystam z algorytmu sortujacego HeapSort o tej wlasnie zlozonosci.
Jednoczesnie w moim rozwiazaniu stosuje optymalizacje, dzieki ktorej nie sortuje nieistotnych dla wyniku elementow o malej wartosci.'''
from kolutesty import runtests

def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2
def heapify(T,i,n):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and T[l]>T[max_ind]:
        max_ind=l
    if r<n and T[r]>T[max_ind]:
        max_ind=r
    if max_ind!=i:
        T[i],T[max_ind]=T[max_ind],T[i]
        heapify(T,max_ind,n)

def buildheap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,i,n)

def ice_cream(T):
    n=len(T)
    buildheap(T)
    #Liczenie wyniku z wykorzystaniem tego, ze na gorze kopca zawsze jest najwieksza wartosc, do ktorej jeszcze nie doszlismy
    wynik,ilosc=0,0
    for i in range(n-1,0,-1):
        if T[0]-ilosc>0:
            wynik+=T[0]-ilosc
            ilosc+=1
            T[0],T[i]=T[i],T[0]
            heapify(T,0,i)
        else:
            break
    return wynik

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ice_cream,all_tests=True)