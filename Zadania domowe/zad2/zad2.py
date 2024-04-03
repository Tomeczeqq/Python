''' Tomasz Janeczko 414613
Dane wejsciowe: tablica S o rozmiarze n zawierajaca liczby naturalne
Szukane: maksymalna mozliwa ilosc sniegu do wywiezienia
Opis rozwiazania:
Na poczatku stworzymy kopiec z elementow z tablicy S. Zwrocmy uwage na to, ze istotny dla nas jest zysk przez wziecie danego elementu do
naszego rozwiazania. Ten zysk jest rowny wartosci tego elementu minus ilosci wszystkich wczesniejszych wzietych elementow (przez zjawisko
topnienia sniegu i wybor kolejnego zmniejsza nam sie wartosci sniegow w momencie ich wziecia). Do naszego wyniku bierzemy elementy tak
dlugo, jak uzyskany z nich zysk jest dodatni. Zauwazmy, ze w trakcie sortowania kopcowego,z ktorego korzystamy, zawsze na gorze jest
najwieksza wartosc, ktorej jeszcze nie przejrzelismy, co jest dla nas bardzo korzystne, poniewaz dzieki temu mozemy wykorzystac
optymalizacje, ktora opiera sie na tym ze nie bedziemy sortowac najmniejszych elementow w kopcu (nie jest to przydatne), tylko bierzemy
najwiekszy (chwilowy) element i sprawdzamy czy zysk z niego jest dodatni. Jesli nie, to mozemy zakonczyc przegladanie naszego kopca,
poniewaz kazdy kolejny element jest niewiekszy od tego, ktory zysk jest niedodatni, wiec on tez bedzie niedodatni.
Poprawność rozwiazania:
Mozemy posortowac tablice S nie zwracajac uwage na indeksy, poniewaz zgodnie z opisem rozwiazania mozemy isc od lewej czy prawej strony.
Zauwazmy, ze nie ma to dla nas wiekszego znaczenia, poniewaz kazdy element ma wartosc niemniejsza niz ilosc elemntow (unikamy sytuacji
roztopienia tego elementu, zanim maszyna wezmie z niego snieg), przez co mozemy dowolnie isc nie myslac o wybranej kolejnosci,
bowiem dla kazdego wyboru strony, z ktorej pracujemy, uzyskany wynik jest taki sam. Samo rozwiazanie jest poprawne, poniewaz zawsze
bierzemy element, ktory ma dodatni zysk (mimo, ze inne elementy straca w tym czasie po 1 snieg, to i tak oplaca nam sie go wziac).
Szacowana złożoność obliczeniowa:
Szacuje moja zlozonosc obliczeniowa na O(nlogn), poniewaz korzystam z algorytmu sortujacego HeapSort o tej wlasnie zlozonosci.
Jednoczesnie w moim rozwiazaniu stosuje optymalizacje, dzieki ktorej nie sortuje nieistotnych dla wyniku elementow o malej wartosci.'''
from zad2testy import runtests

def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2
def heapify(S,i,n):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and S[l]>S[max_ind]:
        max_ind=l
    if r<n and S[r]>S[max_ind]:
        max_ind=r
    if max_ind!=i:
        S[i],S[max_ind]=S[max_ind],S[i]
        heapify(S,max_ind,n)

def buildheap(S):
    n=len(S)
    for i in range(parent(n-1),-1,-1):
        heapify(S,i,n)

def snow(S):
    n=len(S)
    buildheap(S)
    #Liczenie wyniku z wykorzystaniem tego, ze na gorze kopca zawsze jest najwieksza wartosc, do ktorej jeszcze nie doszlismy
    wynik,ilosc=0,0
    for i in range(n-1,0,-1):
        if S[0]-ilosc>0:
            wynik+=S[0]-ilosc
            ilosc+=1
            S[0],S[i]=S[i],S[0]
            heapify(S,0,i)
        else:
            break
    return wynik

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow,all_tests=True)