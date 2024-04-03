''' Tomasz Janeczko 414613
Dane wejsciowe: Lista dopuszczalnych przelotow wraz z czasem oraz planety znajdujace sie kolo osobliwosci, czyli w odleglosci 0
od siebie oraz planeta poczatkowa i koncowa i ilosc planet
Szukane: Najkrótszy czas podróży z planety a do planety b albo w.p.p. None
Opis rozwiazania:
Najpierw tworze na podstawie listy dopuszczalnych graf nieskierowany, w ktorym przechowuje (wierch docelowy, czas podrozy).
Nastepnie na podstawie kola osobliwosci tworze miedzy kazdym wierzcholkiem z tego kola krawedzie z kazdym kolejnym wierzcholkiem
o czasie podrozy 0 - wazne jest to, ze nie potrzebujemy tworzyc wszystkich krawedzi miedzy nimi. Nastepnie na tym grafie wykonuje
algorytm Dijsktry, ktory liczy najkrotszy czas podrozy z planety a do b.
Poprawność rozwiazania:
Moje rozwiazanie jest poprawne, poniewaz na poczatku tworze w moim grafie kazda istniejaca znaczaca krawedz i nastepnie wykonuje
na nim algorytm Dijkstry, ktory wyznacza najkrotsza dlugosc sciezki w grafie.
Szacowana złożoność obliczeniowa:
Moj algorytm ma zlozonosc O(ElogV), poniewaz wykonuje algorytm Dijkstry na grafie reprezentowanym przez listy sasiedztwa.'''
from zad5testy import runtests
from queue import PriorityQueue

def Dijkstra(G,n,a,b):
    Q=PriorityQueue()
    d=[float('inf') for i in range(n)]
    d[a]=0
    for i in range(n):
        Q.put((d[i],i))
    while not Q.empty():
        odl,u=Q.get()
        for i in range(len(G[u])):
            neighbor=G[u][i][0]
            temp=odl+G[u][i][1]
            if temp<d[neighbor]:
                d[neighbor]=temp
                Q.put((d[neighbor],neighbor))
    if d[b]!=float('inf'):
        return d[b]
    return None

def spacetravel(n,E,S,a,b):
    #Stworzenie grafu reprezentowanego przez listy sasiedztwa
    G=[[]for i in range(n)]
    for i in range(len(E)):
        x,y,time=E[i][0],E[i][1],E[i][2]
        G[x].append((y,time))
        G[y].append((x,time))
    for i in range(len(S)-1):
        x,y,time=S[i],S[i+1],0
        G[x].append((y,time))
        G[y].append((x,time))
    G[S[0]].append((S[len(S)-1],0))
    G[S[len(S)-1]].append((S[0],0))
    return Dijkstra(G,n,a,b)

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel,all_tests=True)