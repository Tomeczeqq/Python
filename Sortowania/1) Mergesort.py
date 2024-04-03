#Sortowanie MergeSort - przez scalanie - od najmniejszego
def merge(S,l,m,r):
    A,B=S[l:m+1],S[m+1:r+1]
    i,j=0,0
    k1,k2=len(A),len(B)
    while l<r:
        if i==k1 or j==k2:
            break
        elif A[i]<B[j]:
            S[l]=A[i]
            i+=1
        else:
            S[l]=B[j]
            j+=1
        l+=1
    #Scalanie reszty znakow - dolaczenie na koniec
    while i<k1:
        S[l]=A[i]
        i+=1
        l+=1
    while j<k2:
        S[l]=B[j]
        j+=1
        l+=1

def mergesort(S,l,r):
    if l<r:
        m=(l+r)//2
        mergesort(S,l,m)
        mergesort(S,m+1,r)
        merge(S,l,m,r)
    return T

T=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(mergesort(T,0,len(T)))
