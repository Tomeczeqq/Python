#Sortowanie HeapSort - przez kopcowanie - od najmniejszego
def parent(index): return (index-1)//2
def left(index): return 2*index+1
def right(index): return 2*index+2

#Naprawianie struktury kopca
def heapify(T,i,n):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and T[l]>T[max_ind]:
        max_ind=l
    if r<n and T[r]>T[max_ind]:
        max_ind=r
    if max_ind!=i:
        T[i],T[max_ind]=T[max_ind],T[i]
        heapify(T,max_ind,n)

#Budowa kopca
def buildheap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,i,n)

#Sortowanie tablicy dzieki strukturze kopca - zawsze na gorze jest najwiekszy niewykorzystany element
def heapsort(T):
    n=len(T)
    buildheap(T)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]
        heapify(T,0,i)
    return T

T=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(heapsort(T))

'''#Kopiec jako kolejka priorytetowa: insert, extract_max
#Wstawianie na kopiec zachowujac kolejnosc posortowania
def insert(T,value):
    i=len(T)
    p=parent(i)
    T.append(value)
    #size+=1
    while p>=0:
        if T[p]<T[i]:
            T[p],T[i]=T[i],T[p]
        else:
            return
        i=p
        p=parent(p)
        heapify(T,p,len(T))
        p=parent(p)

insert(T,8)
print(T)
#Wziecie najwiekszego elementu
def extract_max(T):
    max=T[0]
    T[0]=T[len(T)-1]
    print(T)
    T.pop()
    print(T)
    heapify(T,0,len(T))
    print(T)
    return max

#print(extract_max(T))
#print(T)'''