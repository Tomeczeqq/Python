'''Tomasz Janeczko 414613
Opis rozwiazania:
W moim rozwiazaniu najpierw tworze pomocnicza tablice Pom, ktora bedzie zawierala zawsze poczatkowa kolejnosc elementow w tablicy T.
Nastepnie wyliczam sobie z0 korzystajac z czesciowo posortowanej tablicy. Pozniej dla kazdego elementu sprawdzam, czy zmienia on wartosc
tego, jaki powinien byc teraz k-ty najwiekszy element przy wyliczanym zi. Moj algorytm dziala az do wyliczenia ostatniej wartosci zn-p.
Poprawnosc rozwiazania:
Jest to rozwiazanie poprawne, poniewaz zawsze bierzemy k-ty najwiekszy element dla kazdego kolejnego przedzialu. W zaleznosci od
wartosci Pom[i+p-1], albo wyliczamy wartosc k-tego najwiekszego elementu, albo wykorzystujemy wiedze z poprzedniego podwyniku.
Szacowana zlozonosc obliczeniowa:
Moja zlozonosc obliczeniowa szacuje na O(nplogp),poniewaz w pesymistycznym wariancie uruchamiam n-p+1 razy quicksorta na
przedzialach o dlugosci p (co ograniczamy od gory przez n).'''
from kol1testy import runtests

def partition(T,l,r):
    if l>=r:
        return l
    pivot=T[r]
    j=l
    for i in range(l,r):
        if T[i]<pivot:
            T[i],T[j]=T[j],T[i]
            j+=1
    T[r],T[j]=T[j],T[r]
    return j

def quicksort(T,l,r):
    if l<r:
        pivot=partition(T,l,r)
        quicksort(T,l,pivot-1)
        quicksort(T,pivot+1,r)

def ksum(T, k, p):
    n=len(T)
    result=0
    Pom=T.copy()
    quicksort(T,0,p-1)
    result+=T[p-k]
    previous=T[p-k]
    #Idziemy po wszytkich zi od 1 do n-p tak aby uzyskac sume z z(0) do z(n-p)
    for i in range(1,n-p+1):
        if Pom[i-1]>previous and Pom[i+p-1]>previous:
            result+=previous
        elif Pom[i-1]<previous and Pom[i+p-1]<previous:
            result+=previous
        else:
            T=Pom.copy()
            quicksort(T,i,i+p-1)
            previous=T[i+p-k]
            result+=previous
    return result

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum,all_tests=True)