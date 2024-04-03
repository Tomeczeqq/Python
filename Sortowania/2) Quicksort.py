#Sortowanie QuickSort - szybkie - od najmniejszego
def partition(T,l,r):
    if l>=r:
        return l
    pivot=T[r]                  #Jest to najbezpieczniejszy wybor pivota, ale moze byc tez losowy lub mediana 3 wybranych liczb
    j=l
    for i in range(l,r):
        if T[i]<pivot:
            T[i],T[j]=T[j],T[i]
            j+=1
    T[r],T[j]=T[j],T[r]
    return j

#Pierwszy jest to klasyczny QuickSort
def quicksort(T,l,r):
    if l<r:
        pivot=partition(T,l,r)
        quicksort(T,l,pivot-1)
        quicksort(T,pivot+1,r)
    return T

T=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(quicksort(T,0,len(T)-1))

#Drugi jest to Quicksort bez tzw. rekurencji ogonowej
def quicksort_bez_rek(T,l,r):
    while l<r:
        q=partition(T,l,r)
        quicksort_bez_rek(T,l,q-1)
        l=q+1
    return T

T2=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(quicksort_bez_rek(T2,0,len(T2)-1))

#Trzeci jest to Quicksort z pamiecia zajmujaca O(log n) - wywolujemy sie rekurencyjnie tylko od krotszej czesci: w najlepszym wypadku
#(wybierania zawsze pivota w srodku), to mamy wtedy log n pamieci zajetej
def quicksort_logn(T,l,r):
    while l<r:
        pivot=partition(T,l,r)
        if r-pivot>pivot-l:                                 #prawa czesc od pivota jest krotsza
            quicksort_logn(T,l,pivot-1)
            l=pivot+1
        else:                                               #lewa czesc od pivota jest krotsza
            quicksort_logn(T,pivot+1,r)
            r=pivot-1
    return T

T3=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(quicksort_logn(T3,0,len(T3)-1))