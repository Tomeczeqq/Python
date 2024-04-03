#Jest to algorytm BFS - wrzuca po kolei wierzcholki do kolejki - fale powstajace po rzucie kamienia
#Zlozonosc wynosi: dla list sasiedztwa O(V+E), dla macierzowej O(V^2)
#1-sze zastosowania: znajdowanie najkrotszych sciezek w sensie krawedzi, sprawdzenie spojnosci grafu
from queue import Queue

def BFS(G,p):
    Q=Queue()
    n=len(G)
    visited,d,parent=[False for v in range(n)],[-1 for v in range(n)],[None for v in range(n)]
    visited[p],d[p]=True,0
    Q.put(p)
    while not Q.empty():
        u=Q.get()
        for v in range(len(G[u])):
            neighbor=G[u][v]
            if visited[neighbor]==False:
                visited[neighbor],d[neighbor],parent[neighbor]=True,d[u]+1,u
                Q.put(neighbor)
    #Wypisywanie odleglosci miedzy wierzcholkiem startowym a kazdym innym
    for i in range(n):
        if i is not p:
            print("Wierzcholek: ",i," odleglosc: ",d[i])
    #Sprawdzenie spojnosci grafu - skladnia for & else
    for i in range(n):
        if visited[i]==False:
            print("Graf nie jest spojny")
            break
    else:
        print("Graf jest spojny")

#2-gie zastosowania: dwudzielnosc, wykrywanie cykli (dotarcie do odwiedzonego wierzcholka nie bedacego parentem aktualnego wierzch)
def BFS_2(G,p):
    Q=Queue()
    n=len(G)
    bipartite,d,parent=[0 for v in range(n)],[-1 for v in range(n)],[None for v in range(n)]
    biparticular,acyclic,bipartite[p],d[p]=True,True,1,0
    Q.put(p)
    while not Q.empty():
        u=Q.get()
        for v in range(len(G[u])):
            neighbor=G[u][v]
            if bipartite[neighbor]==0:
                bipartite[neighbor]=3-bipartite[u]
                d[neighbor],parent[neighbor]=d[u]+1,u
                Q.put(neighbor)
            else:
                if bipartite[u]==bipartite[neighbor]:
                    biparticular=False
                if parent[u]!=neighbor:
                    acyclic=False
    #Sprawdzenie czy graf jest dwudzielny
    if biparticular is True:
        print("Graf jest dwudzielny")
    else:
        print("Graf nie jest dwudzielny")
    #Sprawdzenie czy graf jest acykliczny
    if acyclic is True:
        print("Graf nie posiada cykli")
    else:
        print("Graf posiada cykle")

#G=[[1,2],[0,2],[0,1]]
#G=[[1,2],[0,2,3],[0,1],[1]]
#G=[[1,2,3],[0,3],[0,3],[0,1,2]]
#G=[[1],[2],[0],[]]
G=[[1],[0,2],[1,3],[2]]
p=0
BFS(G,p)
BFS_2(G,p)