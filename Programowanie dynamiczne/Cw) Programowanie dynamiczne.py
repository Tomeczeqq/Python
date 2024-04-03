#Black Forest - maksymalny zysk gdy nie mozemy wyciac dwoch drzew kolo siebie, gdzie ci - zysk wyciecia i-tego drzewa
def blackforest(C):
    n=len(C)
    f=[-1 for i in range(n)]
    if n==0:
        return 0
    if n==1:
        return C[0]
    f[0]=C[0]
    f[1]=max(C[0],C[1])
    for i in range(2,n):
        f[i]=max(f[i-1],f[i-2]+C[i])
    return f[n-1]

#Spadajace klocki - zawierajace sie przedzialy [a,b]
#g(i) - ograniczenia przedzialu dla i-tego klocka
#f(0)=0,   f(i)=min(f(i-1)+1, min j<i (f(j) + (i-j+1) gdy g(j) zawiera sie w [ai,bi]
def upper(a,b):
    if a[0]<b[0] or a[1]>b[1]:
        return False
    return True

def fallingblock(T,cache,top,i):
    if i==0:
        top[0]=T[0]
        return 0
    if cache[i]!=-1:
        return cache[i]
    cache[i]=min(fallingblock(T,cache,top,i-1)+1,
                 min([fallingblock(T,cache,top,j) + (i-j+1) for j in range(i) if upper([T[i],top[j]])]),
                 i)
    if cache[i]==fallingblock(T,cache,top,i-1)+1:
        top[i]=top[i-1]
    else:
        top[i]=T[i]
    return cache[i]

def fallingblock2(T,n):
    cache,top=[-1 for i in range(n)],[None for i in range(n)]
    cache[0]=0
    top[0]=T[0]
    return fallingblock(T,cache,top,n)

#Ladowanie promu - tablica A[n] z dlugosciami samochodow
#Kazdy samochod wjezdza na prawy lub lewy pas (oba dlugosci L) - ktore samochody powinny wjechac na ktory pas, aby zmiescilo sie
#jak najwiecej aut na promie; auta musza wjezdzac w takiej kolejnosci jak podane w tablicy A