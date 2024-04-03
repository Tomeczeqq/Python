#BucketSort - sortowanie kubelkowe Θ(n) - tworzymy n kubelkow o rozmirze [i/n,(i+1)/n) i sortujemy kazdy z kubelkow
#oraz nastepnie przepisujemy dane z kubelkow w kolejnosci posortowanej
def bubblesort(T):
    n=len(T)
    for i in range(n):
        for j in range(i+1,n):
            if T[i]>T[j]:
                T[i],T[j]=T[j],T[i]

def bucketsort(T):
    n=len(T)
    B,K=[[None for i in range(n)] for i in range(n)],[0 for i in range(n)]
    for i in range(n):
        a=int((T[i]*n)//1)
        B[a][K[a]]=T[i]
        K[a]+=1
    for i in range(n):
        B[i]=B[i][0:K[i]]
        bubblesort(B[i])
    j=0
    for i in range(n):
        x=0
        while x<len(B[i]):
            T[j]=B[i][x]
            x+=1
            j+=1
    return T

T=[0.14,0.19,0.73,0.24,0.21,0.68,0.94,0.33,0.3,0.2]
T2=[0.12,0.998,0.2,0.5,0.13,0.434,0.22,0.94,0.806,0.13,0.68,0.27,0.33,0.56,0.702,0.34,0.578,0.444,0.208,0.3,0.7]
print(bucketsort(T))
print(bucketsort(T2))

#CountingSort - stabilne sortowanie przez zliczanie Θ(n+k) - dla tablicy zawierajacej liczby naturalne z zakresu {t,...,t+k-1}
#k - rozpietosc danych = (max_value-min_value+1)
def countingsort(A,k):
    n=len(A)
    B=[0 for i in range(n)]
    C=[0 for i in range(k)]
    for i in range(n):
        C[A[i]]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        C[A[i]]-=1
        B[C[A[i]]]=A[i]
    for i in range(n):
        A[i]=B[i]
    return B

T3=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(countingsort(T3,66))

#RadixSort - sortowanie pozycyjne n slow o dlugosci t, gdzie t to dlugosc kazdego ze slow o czasie Θ(n*t)
#Sortujemy po kolei od TYLU kazda kolumna i tak uzykujemy posortowanie danych
def counting_sort_position(T,digit_idx):
    count=[0]*10
    for num in T:
        digit=(num//(10**digit_idx))% 10
        count[digit]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    n=len(T)
    TS=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        num=T[i]
        digit=(num//(10**digit_idx))% 10
        TS[count[digit]-1]=num
        count[digit]-=1
    for i in range(n):
        T[i]=TS[i]

def radix_sort(T):
    number_of_digits=len(str(max(T)))
    for digit_idx in range(number_of_digits):
        counting_sort_position(T,digit_idx)
    return T

T4=[1,2,4,5,1,3,2,5,4,3,65,35,33,33,34,7,1,0,8,9]
print(radix_sort(T4))