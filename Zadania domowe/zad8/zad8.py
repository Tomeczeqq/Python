''' Tomasz Janeczko 414613
Dane wejsciowe: Dwuwymiarowa tablica liczb naturalnych T, w której wartość T[u][v] to objętość ropy na polu o współrzędnych (u, v)
Szukane: Minimalna liczba zatrzymań cysterny potrzebna do przejechania trasy (cysterna porusza się tylko po polach (0,v))
Opis rozwiazania:
Najpierw wyznacze jak sporo ropy mozna zebrac z kazdego punktu na trasie (jesli jest kilka pol na trasie kolo siebie to wtedy
wartosc nadaje temu najbardziej po lewej stronie, poniewaz tam moze sie najbardziej przydac). Nastepnie biore i ide do przodu jak
najdalej moge po trasie jednoczesnie wrzucajac do kolejki priorytetowej (high-priority) wszystkie mozliwe na aktualny moment plamy.
Poprawność rozwiazania:
Moje rozwiazanie jest poprawne, poniewaz uwzgledniam w nim wszystkie mozliwe plamy znajdujace sie na trasie w jak najlepszym
polozeniu (najbardziej na lewo) i wybieram aktualnie mozliwie jak najwieksze plamy do wziecia az do dotarcia do konca trasy.
Szacowana złożoność obliczeniowa:
Moja zlozonosc obliczeniowa szacuje na O(nm+n), poniewaz najpierw liczac wartosci pol na trasie mozliwe jest przejscie po
wszystkich polach, a pozniej przechodze po trasie liczac juz koncowy wynik.'''
from zad8testy import runtests
from queue import Queue
from queue import PriorityQueue

def plan(T):
    n,m=len(T[0]),len(T)
    for i in range(n):
        if T[0][i]!=0:
            ropa=T[0][i]
            T[0][i]=0
            Q=Queue()
            Q.put((0,i))
            while not Q.empty():
                a,b=Q.get()
                if a>0 and T[a-1][b]>0:
                    ropa+=T[a-1][b]
                    T[a-1][b]=0
                    Q.put((a-1,b))
                if a<m-1 and T[a+1][b]>0:
                    ropa+=T[a+1][b]
                    T[a+1][b]=0
                    Q.put((a+1,b))
                if b>0 and T[a][b-1]>0:
                    ropa+=T[a][b-1]
                    T[a][b-1]=0
                    Q.put((a,b-1))
                if b<n-1 and T[a][b+1]>0:
                    ropa+=T[a][b+1]
                    T[a][b+1]=0
                    Q.put((a,b+1))
            T[0][i]=ropa
    wynik,plamy=1,T[0][0]
    PQ=PriorityQueue()
    for i in range(1,n-1):
        plamy-=1
        if T[0][i]>0:
            PQ.put(-T[0][i])
        if plamy==0:
            plamy=-PQ.get()
            wynik+=1
    return wynik

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan,all_tests=True)