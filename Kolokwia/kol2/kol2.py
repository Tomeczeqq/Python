''' Tomasz Janeczko 414613
Opis rozwiazania:
Latwo mozemy zauwazyc, ze podstawowywm warunkiem istnienia w tym zadaniu drzewa pieknego jest to, ze istnieje jakies MST, ktorego
krawedzie skladaja sie z kolejnych wartosci wag krawedzi. Jesli takie drzewo nie istnieje to wowczas odpowiedzia jest None.
W moim rozwiazaniu wybieram po kolei od najmniejszych mozliwych krawedzi wszystkie kolejne V-1 krawedzi sprawdzajac, czy nie
powstanie jednoczesnie cykl.
Poprawność rozwiazania:
Moje rozwiazanie jest poprawne, poniewaz zawsze znalezione rozwiazanie jest najmniejsze, poniewaz sprawdzam wszystkie warianty,
ktore spelniloby rozwiazanie zadanie poczawszy od wariantow, ktorych wynik jest potencjalnie najmniejszy, czyli szukany.
Szacowana złożoność obliczeniowa:
Moja zlozonosc obliczeniowa szacuje na O(EVlog*E), poniewaz w pesymistycznym wariancie przechodze i sprawdzam dla kazdej krawedzi
(do V-E) czy biorac po kolei wszystkie kolejne (V-1) krawedzi otrzymam drzewo MST. Jednoczesnie korzystam z operacji FIND/UNION,
ktore posiadaja zlozonosc log*E.'''
from kol2testy import runtests
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

def beautree(G):
    #Stworzenie listy ze wszystkimi krawedziami oraz posortowanie jej po wagach krawedzi
    V=len(G)
    Edges=[]
    for u in range(V):
        for v,w in G[u]:
            if u<v:
                Edges.append([u,v,w])
    Edges.sort(key=lambda x:x[2])
    #Faktyczne wykorzystanie algorytmu Kruskala
    E=len(Edges)
    for i in range(E-V+1):
        edge_count,result=0,0
        parent,rank=[i for i in range(V)],[0 for v in range(V)]
        for j in range(i,E):
            u,v,w=Edges[j]
            result+=w
            x,y=find(parent,u),find(parent,v)
            if x!=y:
                union(parent,rank,x,y)
                edge_count+=1
                if edge_count==V-1:
                    return result
            else:
                break
    return None

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree,all_tests=True)