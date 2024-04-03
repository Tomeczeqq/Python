#Jest to algorytm DFS - idzie wzdluz obranej sciezki tak dlugo jak jest to mozliwe
#Zlozonosc wynosi: dla list sasiedztwa O(V+E), dla macierzowej O(V^2)
#1-sze zastosowanie: znajdowanie najkrotszych sciezek w sensie krawedzi, spojnosc
def DFS_1(G,p,visited,d,parent,n):
    for v in range(len(G[p])):
        neighbor=G[p][v]
        if visited[neighbor]==False:
            visited[neighbor],d[neighbor],parent[neighbor]=True,d[p]+1,p
            DFS_1(G,neighbor,visited,d,parent,n)
        elif visited[neighbor]==True and d[neighbor]>d[p]+1:           #Poprawienie odleglosci dla odwiedzonego
            d[neighbor],parent[neighbor]=d[p]+1,p
            DFS_1(G,neighbor,visited,d,parent,n)

def DFS_decl_1(G,p):
    n=len(G)
    visited,d,parent=[False for v in range(n)],[-1 for v in range(n)],[None for v in range(n)]
    visited[p],d[p]=True,0
    DFS_1(G,p,visited,d,parent,n)
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

#G=[[1,2],[0,2],[0,1]]
#G=[[1,2],[0,2,3],[0,1],[1]]
#G=[[1,2,3],[0,3],[0,3],[0,1,2]]
#G=[[1],[2],[0],[]]
#G=[[1],[0,2],[1,3],[2]]
#G=[[1,2],[0,2],[0,1,3],[2]]
G=[[1,2],[0,3],[0,4],[1],[2]]
print("1-sze zastosowanie:")
DFS_decl_1(G,0)

#2-gie zastosowanie: dwudzielnosc, wykrywanie cykli
def is_bipartite(G):
    n=len(G)
    colors,stack,visited=[None for v in range(n)],[],[False for v in range(n)]
    def assign_color(v,color):
        if colors[v] is not None:
            return colors[v]==color
        colors[v]=color
        return True
    for start_vertex in range(n):
        if not visited[start_vertex]:
            stack.append((start_vertex,0))
            while stack:
                current_vertex,color=stack.pop()
                visited[current_vertex]=True
                if not assign_color(current_vertex,color):
                    return False
                for neighbor in G[current_vertex]:
                    if not visited[neighbor]:
                        stack.append((neighbor,1-color))
    return True

def has_cycle(G):
    n=len(G)
    def dfs(v,visited,parent):
        visited[v]=True
        for neighbor in G[v]:
            if not visited[neighbor]:
                if dfs(neighbor,visited,v):
                    return True
            elif neighbor!=parent:
                return True
        return False
    visited=[False for v in range(n)]
    for vertex in range(n):
        if not visited[vertex]:
            if dfs(vertex,visited,None):
                return True
    return False

G=[[1,2],[0,3],[0,3],[1,2,4],[3]]
print("2-gie zastosowanie:")
if is_bipartite(G):
    print("Graf jest dwudzielny")
else:
    print("Graf nie jest dwudzielny")
if has_cycle(G):
    print("Graf posiada cykle")
else:
    print("Graf nie posiada cykli")

#3-cie zastosowanie: sortowanie topologiczne - ulozenie krawedzi takie, ze krawedzie wskazuja wylacznie z lewej strony na prawa
#Sluzy do m.in. wyznaczania kolejnosci realizacji zadan jesli niektore z nich musza byc wykonane przed innymi
def topological_sort(G):
    n=len(G)
    in_degree,result=[0 for v in range(n)],[]
    for neighbors in G:
        for neighbor in neighbors:
            in_degree[neighbor]+=1
    Q=[vertex for vertex in range(n) if in_degree[vertex]==0]
    while Q:
        v=Q.pop(0)
        result.append(v)
        for neighbor in G[v]:
            in_degree[neighbor]-=1
            if in_degree[neighbor]==0:
                Q.append(neighbor)
    if len(result)!=n:
        return None
    return result

G=[[1,2],[3],[3,4],[5],[5],[]]
sorted_order=topological_sort(G)
print("3-cie zastosowanie:")
if sorted_order is None:
    print("Graf zawiera cykle")
else:
    print("Sortowanie topologiczne:",sorted_order)

#4-te zastosowanie: cykl Eulera
#Graf posiada cykl Eulera <=> Graf jest spojny i kazdy jego wierzch jest stopnia parzystego
def has_eulerian_cycle(G):
    stack,path=[0],[]
    while stack:
        current_vertex=stack[-1]
        if G[current_vertex]:
            next_vertex = G[current_vertex].pop(0)
            stack.append(next_vertex)
        else:
            path.append(stack.pop())
    for neighbors in G:
        if neighbors:
            return False  # Graf nie jest spójny
    return True if len(path)==sum(len(neighbors) for neighbors in G)+1 else False

G=[[1,2],[0,2],[0,1]]
print("4-te zastosowanie:")
if has_eulerian_cycle(G):
    print("Graf posiada cykl Eulera")
else:
    print("Graf nie posiada cyklu Eulera")

#5-te zastosowanie: silnie spojne skladowe w grafie skierowanym => Trzeba wykonac dfs-a i revers_dfs-a
def dfs_sss(G,node,visited,stack):
    visited[node]=True
    neighbors=G[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            dfs_sss(G,neighbor,visited,stack)
    stack.append(node)

def reverse_dfs(revG,node,visited,component):
    visited[node]=True
    neighbors=revG[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            reverse_dfs(revG,neighbor,visited,component)
    component.append(node)

def get_strongly_connected_components(graph):
    n=len(graph)
    visited,stack,components=[False for v in range(n)],[],[]
    #Przejście DFS
    for node in range(n):
        if not visited[node]:
            dfs_sss(graph,node,visited,stack)
    #Stworzenie odwróconego grafu
    revG=[[] for v in range(n)]
    for node in range(n):
        neighbors=graph[node]
        for neighbor in neighbors:
            revG[neighbor].append(node)
    visited=[False for v in range(n)]
    #Przejście Reverse DFS
    while stack:
        node=stack.pop()
        if not visited[node]:
            component=[]
            reverse_dfs(revG,node,visited,component)
            components.append(component)
    return components

Gs=[[1],[2,4],[0,3],[2,4],[5],[6],[4]]
strongly_connected_components=get_strongly_connected_components(Gs)
print("5-te zastosowanie:")
for component in strongly_connected_components:
    print(component)

#6-te zastosowanie: mosty/punkty artykulacji w grafach nieskierowanych
#Krawedz e jest mostem <=> Nie lezy na zadnym cyklu prostym w grafie; low(v) - identyfikator cyklu
def dfs(G,node,parent,visited,discovery,low,bridges):
    visited[node]=True
    discovery[node]=low[node]=dfs.counter
    dfs.counter+=1
    for neighbor in G[node]:
        if not visited[neighbor]:
            dfs(G,neighbor,node,visited,discovery,low,bridges)
            low[node]=min(low[node],low[neighbor])
            if low[neighbor]>discovery[node]:
                bridges.append((node,neighbor))
        elif neighbor!=parent:
            low[node]=min(low[node],discovery[neighbor])

def find_bridges(G):
    n=len(G)
    visited,discovery,low,bridges=[False for v in range(n)],[-1 for v in range(n)],[-1 for v in range(n)],[]
    dfs.counter = 0
    for node in range(n):
        if not visited[node]:
            dfs(G,node,-1,visited,discovery,low,bridges)
    return bridges

Gm=[[1,2], [0,2,3,4], [0,1], [1,4], [1,3,5], [4,6], [5]]
bridges=find_bridges(Gm)
print("6-te zastosowanie:")
for bridge in bridges:
    print(bridge)

#7-me zastosowanie: tworzenie drzewa DFS za pomoca czasu czasu przetworzenia
def Classic_dfs(G):
    n=len(G)
    visited,parent=[False for v in range(n)],[None for v in range(n)]
    entry_time,exit_time=[-1 for v in range(n)],[-1 for v in range(n)]
    time=0
    def dfs_visit(v):
        nonlocal time
        visited[v]=True
        time+=1
        entry_time[v]=time
        for neighbor in G[v]:
            if not visited[neighbor]:
                parent[neighbor]=v
                dfs_visit(neighbor)
        time+=1
        exit_time[v]=time
    for v in range(n):
        if not visited[v]:
            dfs_visit(v)
    return parent,entry_time,exit_time

parent,entry_time,exit_time=Classic_dfs(G)
print("7-me zastosowanie:\nParent:", parent,"\nEntry time:", entry_time,"\nExit time:", exit_time)