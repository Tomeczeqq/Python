#Sortowanie Combsort - grzebieniowe
#Opiera sie na metodzie babelkowej i ma zlozonosc O(nlogn). Statystycznie dziala wolniej niz Quicksort, ale jest prostszy.

def Combsort(T):
    swappped=True
    n=len(T)
    gap=n
    while gap>1 or swapped:
        gap=max(int(gap /1.3),1)
        top=n-1-gap
        swapped=False
        for i in range(top+1):
            j=i+gap
            if T[i]>T[j]:
                T[i],T[j]=T[j],T[i]
                swapped=True
    return T

T=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(Combsort(T))