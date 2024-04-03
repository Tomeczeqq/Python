''' Tomasz Janeczko 414613
Dane wejsciowe: Graf nieskierowany G=(V,E) oraz dwa wiercholki s,t ∈ V
Szukane: krawedz, której usunięcie z E spowoduje wydłużenie najkrótszej ścieżki między s oraz t albo w.p.p. None
Opis rozwiazania:
W moim rozwiazaniu najpierw algorytmem BFS wyznaczam najkrotsza sciezke do wierzcholka koncowego. Nastepnie po kolei probuje
usuwac kazda kolejna krawedz z tej sciezki i jesli nowa odleglosc do wierzcholka t jest inna, to wtedy znalazlem jeden z wynikow.
Poprawność rozwiazania:
Jest to rozwiazanie poprawne, poniewaz dla kazdej mozliwosci usuniecia krawedzi ze sciezki sprawdzam, czy rzeczywiscie jej
usuniecie zmieni odleglosc do wierzcholka t, co jest wowczas naszym rozwiazaniem.
Szacowana złożoność obliczeniowa:
Zlozonosc obliczeniowa mojego rozwiazania szacuje na O(E*(V+E)),poniewaz w moim algorytmie korzystam maksymalnie E razy
z algorytmu BFS o zlozonosci O(V+E) (dla list sasiedztwa, z ktorych korzystam w mojej implementacji).'''
from zad4testy import runtests
from queue import Queue

def BFS_pierw(G,s,t):
    Q=Queue()
    n=len(G)
    d,parent=[-1 for v in range(n)],[None for v in range(n)]
    d[s]=0
    Q.put(s)
    while not Q.empty() and d[t]==-1:
        u=Q.get()
        for v in range(len(G[u])):
            neighbor=G[u][v]
            if d[neighbor]==-1:
                d[neighbor],parent[neighbor]=d[u]+1,u
                Q.put(neighbor)
    path,i=[t],parent[t]
    while i is not None:
        path.append(i)
        i=parent[i]
    return path

def BFS(G,s,t,a,b):
    for i in range(len(G[a])):
        if G[a][i]==b:
            G[a][i]=a
            break
    for i in range(len(G[b])):
        if G[b][i]==a:
            G[b][i]=b
            break
    Q=Queue()
    n=len(G)
    d=[-1 for v in range(n)]
    d[s]=0
    Q.put(s)
    while not Q.empty() and d[t]==-1:
        u=Q.get()
        for v in range(len(G[u])):
            neighbor=G[u][v]
            if d[neighbor]==-1:
                d[neighbor]=d[u]+1
                Q.put(neighbor)
    return d[t]

def longer(G,s,t):
    path=BFS_pierw(G,s,t)
    dlug_sc=len(path)-1
    for i in range(dlug_sc):
        if BFS(G,s,t,path[i],path[i+1])!=dlug_sc:
            return (path[i],path[i+1])
    return None

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer,all_tests=True)