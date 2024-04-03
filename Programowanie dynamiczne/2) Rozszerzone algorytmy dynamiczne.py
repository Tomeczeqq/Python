#1-sze zadanie: Problem plecakowy dynamiczny; f(i,b) - maksymalna suma cen przedm {0,...,i}, ktorych waga nie przekracza b
#W - wagi, P - ceny, B - maksymalna waga
def knapsack(W,P,B):
    n=len(W)
    F=[[0 for b in range(B+1)] for i in range(n)]
    Parent=[[-1 for b in range(B+1)] for i in range(n)]
    for b in range(W[0],B+1):
        F[0][b]=P[0]
        Parent[0][b]=0
    for b in range(B+1):
        for i in range(1,n):
            F[i][b]=F[i-1][b]
            Parent[i][b]=Parent[i-1][b]
            if b-W[i]>=0:
                new_item=F[i-1][b-W[i]]+P[i]
                if new_item>F[i][b]:
                    F[i][b]=new_item
                    Parent[i][b]=i
    items=[]
    i,b=n-1,B
    while i>=0 and b>=0:
        if Parent[i][b]==i:
            items.append(i)
            b-=W[i]
        i-=1
    items.reverse()
    return F[n-1][B],items

W=[2,3,4,5]
P=[3,4,5,6]
B=8
value,items=knapsack(W,P,B)
print("Ostateczna wartość plecaka dla problemu dynamicznego:",value)
print("Wybrane przedmioty:",items)

#2-gie zadanie: problem komiwojażera (TSP - travelling salesperson problem)
#Minimalna suma odleglosci odwiedzenia wszystkich miast zaczynajac i konczac w tym samym miescie
#Wersja bitoniczna - wspolrzedne x parami rozne; f(i,j) - koszt odwiedzenia wszystkich miast od 0 do j zaczynajac w i do j
#Rozwiazanie O(n^2) - jest to rekurencja ze spamietywaniem
'''D[i][j]=d(i,j)
F[i][j]=[[float('inf')for i in range(n)] for j in range(n)]
F[0][1]=D[0][1]'''
def tspb(i,j,F,D):
    if F[i][j]!=float('inf'):                   #Policzona wartosc
        return F[i][j]
    if i==j-1:                                  #Przypadek bardziej skomplikowany - i oraz j w jednej czesci, zas j-1 w drugiej
        best=float('inf')
        for k in range(j-1):
            best=min(best,tspb(k,j-1,F,D)+D[k][j])
        F[i][j]=best
    else:                                       #Przypadek prostszy - i w jednej czesci, zas j-1 oraz j w drugiej
        F[i][j]=tspb(i,j-1,F,D)+D[j-1][j]
    return F[i][j]