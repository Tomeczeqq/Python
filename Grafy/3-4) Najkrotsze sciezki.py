#1)Algorytm Dijkstry - dla grafow nieskierowanych i skierowanych wazonych o nieujemnych krawedziach - skaczemy do najblizszego v
#Zlozonosc wynosi: dla list sasiedztwa O(ElogV), dla macierzowej O(V^2)
def relax(Q,d,parent,a,b,length):
    if d[a]+length<d[b]:
        d[b],parent[b]=d[a]+length,a
        Q.put((d[b],b))

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
    if d[b]!=float('inf'):
        return d[b]
    return None

print("Algorytm Dijkstry:")
G=[[(1,-1),(2,4)], [(2,3),(3,2),(4,2)], [], [(1,1),(2,5)], [(3,-3)]]
p,k=0,4
print("Najkrótsza odległość od",p,"do",k,"wynosi:",Dijkstra(G,p,k))

#2)Algorytm Bellmana-Forda - dla grafow skierowanych wazonych wraz z ujemnymi krawedziami - umozliwia wykrycie ujemnych cykli
#Zlozonosc wynosi: dla list sasiedztwa O(VE), dla macierzowej O(V^3)
def Bellman_ford(G,start):
    n=len(G)
    d,parent=[float('inf') for v in range(n)],[None for v in range(n)]
    d[start]=0
    #Relaksacja krawędzi
    for _ in range(n-1):
        for u in range(n):
            for v,weight in G[u]:
                if d[u]+weight<d[v]:
                    d[v]=d[u]+weight
                    parent[v]=u
    #Sprawdzenie istnienia cykli ujemnych
    for u in range(n):
        for v,weight in G[u]:
            if d[u]+weight<d[v]:
                return None
    return d

#G=[[(1,-1)], [(2,-1)], [(0,-1)]]
G=[[(1,-1),(2,4)], [(2,3),(3,2),(4,2)], [], [(1,1),(2,5)], [(3,-3)]]
p=0
distances=Bellman_ford(G,p)
print("Algorytm Bellmana-Forda:")
if distances is None:
    print("Graf zawiera cykl o ujemnej wadze")
else:
    print("Najkrótsze odległości od wierzchołka",p)
    for v,dist in enumerate(distances):
        print(v,":",dist)

#3)Algorytm Floyda-Warshalla - sluzy do znajdowania najkrótszych ścieżek pomiędzy wszystkimi parami wierzchołków w grafie ważonym
#Zlozonosc wynosi: dla macierzowej O(V^3) - tylko dla takiej reprezentacji piszemy
def Floyd_warshall(G):
    n=len(G)
    D,Parent=[[-1 for i in range(n)] for j in range(n)],[[float('inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        D[i][i]=0
    for u in range(n):
        for v in range(n):
            if G[u][v]!=float('inf'):
                Parent[u][v]=u
            D[u][v]=G[u][v]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k]+D[k][j]<D[i][j]:
                    D[i][j]=D[i][k]+D[k][j]
                    Parent[i][j]=Parent[k][j]
    return D,Parent

G_2=[[0,5,float('inf'),10],
     [float('inf'),0,3,float('inf')],
     [float('inf'),float('inf'),0,1],
     [float('inf'),float('inf'),float('inf'),0]]
distances,parents=Floyd_warshall(G_2)
print("Najkrotsze odleglosci:")
for row in distances:
    print(row)
print("Macierz rodzicow:")
for row in parents:
    print(row)