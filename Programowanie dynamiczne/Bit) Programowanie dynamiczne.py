#Zadanie 1 - ciecie preta, kawalek o okreslonej dlugosci ma okreslona cene, maksymalna cena z kawalka o dlugosci X
def pret(T,X):
    F,Parent=[0 for i in range(X+1)],[0 for i in range(X+1)]
    T.sort()                    #1-szy indeks to dlugosc kawalka, zas 2-gi indeks to cena za taki kawalek
    for i in range(1,X+1):
        j=0
        while j<len(T) and i>=T[j][0]:
            if F[i-T[j][0]]+T[j][1]>F[i]:
                F[i]=F[i-T[j][0]]+T[j][1]
                Parent[i]=i-T[j][0]
            j+=1
    i=X
    print("Dlugosci pretow na ktore mamy podzielic to:",end=' ')
    while i!=0:
        print(i-Parent[i],end=' ')
        i=Parent[i]
    return F[X]

T=[(3,3),(1,1),(5,8),(7,12)]
X=18
print("\nPret o dlugosci",X,"jest warty:",pret(T,X),"\n")

#Zadanie 2 - tablica MxN kosztow wejscia, minimalny koszt dostania sie z (0,0) do (M-1,N-1) idac tylko na dol i w prawo
def podroznik(B):
    n,m=len(B),len(B[0])
    Wynik=[[float('inf') for j in range(m)] for i in range(n)]
    Wynik[0][0]=B[0][0]
    for j in range(1,m):
        Wynik[0][j]=Wynik[0][j-1]+B[0][j]
    for i in range(1,n):
        Wynik[i][0]=Wynik[i-1][0]+B[i][0]
    for i in range(1,n):
        for j in range(1,m):
            Wynik[i][j]=min(Wynik[i-1][j],Wynik[i][j-1])+B[i][j]
    return Wynik[n-1][m-1]

B=[[4,5,2,3,2],
   [3,5,5,7,6],
   [6,7,5,2,6],
   [3,4,1,7,5]]
print("Koszt dotarcia do pola (n-1)x(m-1) wynosi:",podroznik(B),"\n")

#Zadanie 3 - policzenie wszystkich binarnych (0/1) stringow o dlugosci n bez jedynek obok siebie
def binar(n):
    Wynik=[[0,0] for i in range(n)]         #drugi parametr [0/1] - wynik gdy teraz jest [0,1]
    Wynik[0][0]=Wynik[0][1]=1
    for i in range(1,n):
        Wynik[i][0]=Wynik[i-1][0]+Wynik[i-1][1]
        Wynik[i][1]=Wynik[i-1][0]
    return Wynik[n-1][0]+Wynik[n-1][1]

n=4
print("Liczba wszystkich binarnych stringow o dlugosci",n,"bez jedynek kolo siebie wynosi:",binar(n),"\n")

#Zadanie 4 - zwrocenie najdluzszego fragmentu ze stringa, ktory jest palindromem
def palindrom(S):
    n=len(S)
    if n==0:
        return 0
    Dp=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        Dp[i][i]=1
    start,max_length=0,1        #indeks poczatkowy najdluzszego palindromu, dlugosc najdluzszego palindromu
    for i in range(n-1):        #dwuwyrazowe palindromiki
        if S[i]==S[i+1]:
            Dp[i][i+1]=1
            max_length=2
            start=i
    for length in range(3,n+1):
        for i in range(n-length+1):
            j=i+length-1
            if S[i]==S[j] and Dp[i+1][j-1]==1:
                Dp[i][j]=1
                max_length=length
                start=i
    return max_length

S='dcbcdcbebcdcbcd'
print("Dlugosc najdluzszego palindroma to:",palindrom(S),"\n")

#Zadanie 5 - rekurencyjne schody Amazona - tablica A:A[i] - maksymalna dlugosc skoku na nastepna pozycje, na ile sposobow do n-1
def amazon(A):
    n=len(A)
    if n==0:
        return 0
    if n==1:
        return A[0]
    Wynik=[0 for i in range(n)]
    Wynik[0]=A[0]
    for i in range(1,n):
        for j in range(i,min(i+A[i],n)):
            Wynik[j]+=Wynik[i-1]
    return Wynik[n-1]

A = [2, 4, 1, 2, 7, 3, 1]
print("Na pole n-1 mozemy dostac sie",amazon(A),"sposobow\n")

#Zadanie 6 - zad 1 egz 2020 termin 1 - najwieksza wartosc bezwgledna uzyskana podczas dodawania (my minimalizujemy)
#F[i][j] - najwiekszy wynik tymczasowy z dodawania elementow od i-tego do j-tego, F[i][i+1]=T[i]+T[i+1]
#F[i][j]=max(abs(sum(i,j)),min(F[i+1][j],F[i][j-1])) - |suma od i do j|,min(F[i+1][j],F[i][j-1])

#Zadanie 7 - problem coin change (wydawania reszty)
def coin(T,S):
    F=[float('inf') for i in range(S)]
    T.sort()
    for i in range(len(T)):
        if T[i]<S:
            F[T[i]-1]=1
    for i in range(S):
        if F[i]==float('inf'):
            j=0
            while j<len(T) and T[j]<=i:
                F[i]=min(F[i],F[i-T[j]]+1)
                j+=1
    return F[S-1]

T=[1,2,5,10,25]
S=69
print("Podejscie dynamiczne dla problemu coin change:",coin(T,S))