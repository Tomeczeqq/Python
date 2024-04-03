''' Tomasz Janeczko 414613
Opis rozwiazania:
Poprawność rozwiazania:
Szacowana złożoność obliczeniowa:'''
#Metoda Forda-Fulkersona - problem maksymalnego przeplywu miedzy wierzch s oraz t dla grafu skierowanego
#Napisane dla grafu reprezentowanego jako macierz sasiedztwa
#Zlozonosc wynosi O((V+E)*|f*|) gdzie |f*| jest wartoscia maksymalnego przeplywu
def bfs(G,source,sink,Parent):
    n=len(G)
    visited=[False for i in range(n)]
    queue=[]
    queue.append(source)
    visited[source]=True
    while queue:
        u=queue.pop(0)
        for v in range(len(G)):
            if visited[v]==False and G[u][v]>0:
                queue.append(v)
                visited[v]=True
                Parent[v]=u
                if v==sink:
                    return True
    return False

def ford_fulkerson(G,source,sink):
    n=len(G)
    parent=[-1 for i in range(n)]
    max_flow=0
    while bfs(G,source,sink,parent):
        path_flow=float('inf')
        s=sink
        while s!=source:
            path_flow=min(path_flow,G[parent[s]][s])
            s=parent[s]
        max_flow+=path_flow
        v=sink
        while v!=source:
            u=parent[v]
            G[u][v]-=path_flow
            G[v][u]+=path_flow
            v=parent[v]
    return max_flow

G=[[0, 16, 13, 0, 0, 0],
   [0, 0, 10, 12, 0, 0],
   [0, 4, 0, 0, 14, 0],
   [0, 0, 9, 0, 0, 20],
   [0, 0, 0, 7, 0, 4],
   [0, 0, 0, 0, 0, 0]]
source=0
sink=5
max_flow=ford_fulkerson(G,source,sink)
print("Maksymalny przepływ w grafie wynosi:",max_flow)