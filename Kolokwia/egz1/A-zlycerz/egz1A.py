''' Tomasz Janeczko 414613
Opis rozwiazania: W moim rozwiazaniu najpierw odpalam Dijkstre z wierzcholka poczatkowego i wyliczam najmmniejszy koszt dotarcia
do kazdego wierzcholka bez napadania na jakikolwiek zamek. Nastepnie biore i redefiniuje wartosc krawedzi w moim grafie na koszt
jaki bedzie obowiazywal podczas poscigu. Teraz z wierzcholka koncowego t odpalam Dijkstre, ktora wyznacza minimalny koszt dotarcia
z t do kazdego wierzcholka k podczas poscigu. Wynikiem jest najmniejsza wartosc ze wszystkich wierzcholkow:
koszt dotarcia z s do k bez poscigu + koszt dotarcia z k do t podczas poscigu - zysk ze skarbca z napadnietego zamku
Poprawność rozwiazania: Moje rozwiazanie jest poprawne, poniewaz dla kazdego wierzcholka wyliczam wynik po dokonaniu w nim napadu
na zamek i biore minimalna wartosc ze wszystkich wierzcholkow, ktora jest odpowiedzia minimalnego kosztu przejscia dla Zlycerza.
Szacowana złożoność obliczeniowa: Moja zlozonosc obliczeniowa szacuje na O(V^2logV), poniewaz dwa razy wykonuje algorytm Dijkstry
oraz dodatkowo zmieniam recznie wartosci krawedzi'''
from egz1Atesty import runtests
from queue import PriorityQueue

def Dijkstra(G,a,b):
    n=len(G)
    Q=PriorityQueue()
    d,parent=[float('inf') for i in range(n)],[None for i in range(n)]
    d[a]=0
    for i in range(n):
        Q.put((d[i],i))
    while not Q.empty():
        odl,u=Q.get()
        for i in range(len(G[u])):
            neighbor=G[u][i][0]
            temp=odl+G[u][i][1]
            if temp<d[neighbor]:
                d[neighbor],parent[neighbor]=temp,u
                Q.put((d[neighbor],neighbor))
    return d

def gold(G,V,s,t,r):
    n=len(V)
    Pokojowy=Dijkstra(G,s,t)                     #koszt dotarcia z s do kazdego wierzcholka bez napadania zadnego z zamkow
    #Zmiana wartosci krawedzi grafu na te podczas scigania
    for x in range(n):
        for y in range(len(G[x])):
            G[x][y]=(G[x][y][0],2*G[x][y][1]+r)
    Wojenny=Dijkstra(G,t,s)                      #koszt dotaria z t do kazdego wierzcholka podczas gonitwy
    wynik=float('inf')
    for i in range(n):
        wynik=min(wynik,Pokojowy[i]+Wojenny[i]-V[i])
    return wynik

runtests(gold,all_tests=True)