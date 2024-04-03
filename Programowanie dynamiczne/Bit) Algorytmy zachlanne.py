#Zadanie 1 - problem coin change (wydawania reszty)
def coin(T,S):
    T.sort()
    j,wynik=len(T)-1,0
    while S>0 and j>=0:
        if S>=T[j]:
            wynik+=1
            S-=T[j]
        else:
            j-=1
    return wynik

T=[1,2,5,10,25]
S=66
print("Podejscie zachlanne dla problemu coin change:",coin(T,S),"\n")

#Zadanie 2 - przyjazdy i odjazdy pociagow, czy M torow wystarczy gdy (pi,oi) to czas przyjazdu i odjazdu dla i-tego pociagu
from queue import PriorityQueue
def trains(P,M):
    PQ=PriorityQueue()
    for i in range(len(P)):
        PQ.put((P[i][0],'P'))
        PQ.put((P[i][1],'O'))
    counter,res=0,True
    while not PQ.empty():
        ele=PQ.get()
        if ele[1]=='P':
            counter-=1
        else:
            counter+=1
            if counter>M:
                res=False
                break
    if res==True:
        print(M,"tory wystarcza\n")
    else:
        print(M,"tory nie wystarcza\n")

P=[(0,3),(2,7),(3,5)]
M=2
trains(P,M)

#Zadanie 3 - ustawianie maszyn o zasiegu k, czy da sie pokryc wszystkie miasta
def maszyny(F,k):           #F[i]-czy w i-tym miescie mozna postawic maszyne
    i,res=0,0
    while i+k-1<len(F)-1:
        if F[i+k-1]==1:
            i+=k-1
            res+=1
        else:
            temp,j=i,i+k-1
            while j>i:
                if F[j]==1:
                    i=j
                    break
                j-=1
            if j==temp:
                res=-1
                break
    if res==-1:
        print("Nie ma takiego ulozenia maszyn\n")
    else:
        print("Nalezy postawic",res,"maszyn\n")

F=[0,0,1,0,1,0,1,1,1]
k=3
maszyny(F,k)

#Zadanie 4 - string, w ktorym niektore znaki sie powtarzaja->otrzymac najmniejszy leksykograficznie string przez usuniecie dupl.