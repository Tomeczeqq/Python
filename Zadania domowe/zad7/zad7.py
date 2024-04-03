''' Tomasz Janeczko 414613
Dane wejsciowe: Tablica L opisujaca labirynt, po ktorym mozemy sie poruszac w prawo,w gore i na dol
Szukane: Zwrocenie największej liczby komnat, które może odwiedzić Wojownik na swojej drodze albo w.p.p. −1
Opis rozwiazania: Jest wziete od Krzycha'''
from zad7testy import runtests

def maze(L):
    n=len(L)
    dp=[[-1 for i in range(n)] for j in range(n)]
    dp[0][0]=0
    for i in range(1,n):
        if L[i][0]=="#":
            break
        dp[i][0]=dp[i-1][0]+1
    for j in range(1,n):
        i=0
        res=-1
        while i<n:
            if L[i][j]!="#":
                if dp[i][j-1]!=-1:
                    res=max(dp[i][j-1]+1,res)
                dp[i][j]=max(dp[i][j],res)
                res+=1 if res!=-1 else 0
            else:
                res=-1
            i+=1
        i=n-1
        res=-1
        while i>=0:
            if L[i][j]!="#":
                if dp[i][j-1]!=-1:
                    res=max(dp[i][j-1]+1,res)
                dp[i][j]=max(dp[i][j],res)
                res+=1 if res!=-1 else 0
            else:
                res=-1
            i-=1
    return dp[n-1][n-1]

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze,all_tests=True)