#Wyszukiwanie polowkowe, ktore zwraca indeks 1-szego elementu o tej wartosci - dotyczy elementow uporzadkowanych

def bin(T,el):
    p,k=0,len(T)-1
    while p<=k:
        mid=(p+k)//2
        if el>T[mid]:             
            p=mid+1
        else:
            k=mid-1
    if p<len(T) and el==T[p]:
        return p
    return -1                          #Nie znaleziono elementu

T=[1,2,3,4,5,6,6,6,6,7,8,9]
print(bin(T,6))