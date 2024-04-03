#Sortowanie babelkowe - przez prosta zamiane - stabilne
#Lecimy po kolei od przodu do tylu porownujac dwa elementy kolo siebie - jesli zla kolejnosc to zamieniamy
def bubblesort(T):
    n=len(T)
    for i in range(n):
        for j in range(i+1,n):
            if T[i]>T[j]:
                T[i],T[j]=T[j],T[i]
    return T

T=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(bubblesort(T))

#Sortowanie przez wstawianie - stabilne
#Lecimy po calej tablicy: kazdy kolejny element wstawiamy w odpowiednim miejscu w posortowanej czesci naszej tablicy
def insertsort(T):
    n=len(T)
    for i in range(1,n):
        klucz=T[i]
        j=i-1
        while j>=0 and T[j]>klucz:
            T[j+1]=T[j]
            j-=1
        T[j+1]=klucz
    return T

T2=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(insertsort(T2))

#Sortowanie przez proste wybieranie - niestabilne
#Wybieramy minimalny element w nieposortowanej czesci tablicy i wstawiamy na indeks i przechodzacy przez cala tablice
def selectsort(T):
    n=len(T)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if T[j]<T[min]:
                min=j
        T[min],T[i]=T[i],T[min]
    return T

T3=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(selectsort(T3))