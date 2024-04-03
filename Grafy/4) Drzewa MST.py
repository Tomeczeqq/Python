#MST - Minimalne drzewa rozpinajace; problem znajdowania podzbioru krawedzi tworzacego spojny podgraf o minimalnej sumie wag
#1)Algorytm Kruskala - po kolei kazda krawedz o najmniejszej wadze, ktora zwieksza podgraf o nowy wierzcholek
#Zlozonosc wynosi: dla list sasiedztwa O(ElogV)
#Struktura Find - wedrujemy w gore drzewa do korzenia i zwracamy reprezentanta zbioru + kompresujemy te sciezke dajac na 'lidera'
#Struktura Union - dolaczamy korzen jednego drzewa do drugiego i laczymy tzw range mniejszego drzewa do wiekszego
def find(parent,i):
    if parent[i]==i:
        return i
    return find(parent,parent[i])

def union(parent,rank,x,y):
    root_x,root_y=find(parent,x),find(parent,y)
    if rank[root_x]<rank[root_y]:
        parent[root_x]=root_y
    elif rank[root_x]>rank[root_y]:
        parent[root_y]=root_x
    else:
        parent[root_y]=root_x
        rank[root_x]+=1

def kruskal(G):
    V=len(G)
    Edges=[]
    for u in range(V):
        for v,w in G[u]:
            Edges.append((u,v,w))
    Edges.sort(key=lambda x:x[2])
    parent,rank=[i for i in range(V)],[0 for v in range(V)]
    MST=[]
    edge_count=0
    for u,v,w in Edges:
        x,y=find(parent,u),find(parent,v)
        if x!=y:
            MST.append((u,v,w))
            union(parent,rank,x,y)
            edge_count+=1
            if edge_count==V-1:
                break
    return MST

G=[[(1,2),(3,6)], [(0,2),(2,3),(3,8),(4,5)], [(1,3),(4,7)], [(0,6),(1,8),(4,9)], [(1,5),(2,7),(3,9)]]
MST=kruskal(G)
print("Algorytm Kruskala:")
for u,v,weight in MST:
    print(f"({u} - {v}): {weight}")

#2)Algorytm Prima - wyznaczanie rodziny zbiorow rozlacznych przez strukture FIND/UNION (do rodziny zbiorow rozlacznych)
#Zlozonosc wynosi: dla list sasiedztwa O(ElogV)
def prim(G):
    V=len(G)
    MST=[]
    visited=[False for v in range(V)]
    start_vertex=0                          #Mozna wybrac dowolny wierzcholek startowy
    visited[start_vertex]=True
    while len(MST)<V-1:                     #Wykonuj dopóki nie odwiedzono wszystkich wierzchołków
        min_weight,min_edge=float('inf'),None
        for u in range(V):
            if visited[u]:
                for v,weight in G[u]:
                    if not visited[v] and weight<min_weight:
                        min_weight,min_edge=weight,(u,v)
        u,v=min_edge                        #Dodanie znalezionej krawędzi o najmniejszej wadze do MST
        MST.append((u,v,min_weight))
        visited[v]=True
    return MST

G_2=[[(1,2),(3,6)], [(0,2),(2,3),(3,8),(4,5)], [(1,3),(4,7)], [(0,6),(1,8),(4,9)], [(1,5),(2,7),(3,9)]]
MST_2=prim(G_2)
print("Algorytm Prima:")
for u,v,weight in MST_2:
    print(f"({u} - {v}): {weight}")