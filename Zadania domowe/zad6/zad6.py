''' Tomasz Janeczko 414613
Dane wejsciowe: Lista numerów maszyn na których kazdy kolejny pracownik potrafi pracować
Szukane: Maksymalna liczba pracowników, którzy mogą jednocześnie pracować gdy na każdej maszynie pracuje tylko jeden pracownik
Opis rozwiazania: Jest wziete od kogos z Discorda'''
from zad6testy import runtests
from collections import deque

def DFS_path(T,parent,start,stop):
    n=len(T)
    Q=deque()
    visited=[False for v in range(n)]
    visited[start]=True
    Q.append(start)
    while Q:
        el=Q.pop()
        for neighbor in T[el]:
            if not visited[neighbor]:
                parent[neighbor]=el
                if neighbor==stop:
                    return True
                visited[neighbor]=True
                Q.append(neighbor)
    return False

def ford_fulkerson(G,p,value):
    n=len(G)
    parent=[p for v in range(n)]
    max_flow=0
    while DFS_path(G,parent,p,value):
        max_flow+=1
        v=value
        while v!=p:
            u=parent[v]
            G[u].remove(v)
            G[v].append(u)
            v=u
    return max_flow

def binworker(M):
    n=len(M)
    for i in range(n):
        M[i]=[e+n for e in M[i]]
    M.extend([2*n+1] for v in range(n))
    M.append([i for i in range(n)])
    M.append([])
    return ford_fulkerson(M,2*n,2*n+1)

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker,all_tests=True)