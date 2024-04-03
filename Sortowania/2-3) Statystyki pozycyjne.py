#Quickselect - jest to k-ta statystyka pozycyjna, czyli element, ktory bylby na k-tej pozycji po posortowaniu tablicy
#Dla wiekszosci przypadkow ma czas O(n), ale w niektorych rzadkich przypadkach potrafi sie 'ukwadracic'
def partition(T,l,r):
    if l>=r:
        return l
    pivot=T[r]                  #Jest to najbezpieczniejszy wybor pivota, ale moze byc tez losowy lub mediana 3 wybranych liczb
    i=l
    for j in range(l,r):
        if T[j]<pivot:
            T[i],T[j]=T[j],T[i]
            i+=1
    T[i],T[r]=T[r],T[i]
    return i

def quickselect(T,k):
    l,r=0,len(T)-1
    while l<r:
        pivot_index=partition(T,l,r)
        if pivot_index==k-1:
            return T[pivot_index]
        elif pivot_index<k-1:
            l=pivot_index+1
        else:
            r=pivot_index-1

T=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
position=15
print(f"Elementem na pozycji {position} jest: {quickselect(T,position)}")

#Magiczne 5-tki - wybor k-tego elementu w czasie O(n) bez ryzyka 'ukwadratowienia'
#Jest uzyta importowana funckja statistics ale powinna byc okej
def median(T):
    n=len(T)
    TS=T.copy()
    def med_partition(l,r):
        pivot=TS[r]
        i=l
        for j in range(l,r):
            if TS[j]<pivot:
                TS[i],TS[j]=TS[j],TS[i]
                i+=1
        TS[i],TS[r]=TS[r],TS[i]
        return i
    def med_quickselect(l,r,k):
        if l==r:
            return TS[l]
        pivot_index=med_partition(l,r)
        if k==pivot_index:
            return TS[k]
        elif k<pivot_index:
            return med_quickselect(l,pivot_index-1,k)
        else:
            return med_quickselect(pivot_index+1,r,k)
    return med_quickselect(0,n-1,n//2)

def median_of_medians(T,k):
    sublists=[T[i:i+5] for i in range(0,len(T),5)]
    medians=[median(sublist) for sublist in sublists]
    if len(medians)<=5:
        pivot=median(medians)
    else:
        pivot=median_of_medians(medians)
    lower,higher,equal=[i for i in T if i<pivot],[i for i in T if i>pivot],[i for i in T if i==pivot]
    if len(lower)>=k:
        return median_of_medians(lower)
    elif len(lower)+len(equal)>=k:
        return pivot
    else:
        return median_of_medians(higher)

T2=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
position2=15
print(f"Elementem na pozycji {position2} jest: {quickselect(T2,position2)}")