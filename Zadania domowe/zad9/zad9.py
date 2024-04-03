''' Tomasz Janeczko 414613
Dane wejsciowe:
•Tablica O zawierająca pozycje parkingów na trasie z A do B, gdzie O[i] to liczba kilometrów (wzdłuż trasy przejazdu)
od A do i-go parkingu
•Tablica C zawierająca ceny za postój na poszczególnych parkingach, gdzie C[i] to opłata za zatrzymanie na i-ym parkingu
•Maksymalna liczba kilometrów T, którą można przejechać bez zatrzymywania (poza wyjątkiem który mówi, że kierowca może jeden raz
przekroczyć limit T kilometrów jazdy bez zatrzymania i wówczas  może przejechać nie więcej niż 2T kilometrów bez zatrzymania)
•Długość L trasy (liczba kilometrów od A do B wzdłuż trasy przejazdu).
Wszystkie wartości przekazane w tablicach O i C oraz argumenty T i L to dodatnie liczby naturalne
Szukane: Minimalny koszt przejechania z miasta A do miasta B
Opis rozwiazania:
Jest to prosty koncepcyjnie dynamik, ktory wyglada nastepujaco:
DP[i][f] - minimalny koszt dojazdu na i-ty parking jednoczesnie zatrzymujac sie na tym parkingu
- gdy f=0 to nie uzywamy wyjatka w tym miescie, czyli bierzemy min(j=i-T z Dp[j][0])
- gdy f=1 to uzywamy wyjatka w tym miescie i wtedy min(j=i-2T z Dp[j][0], k=i-T z Dp[k][1])
Poprawność rozwiazania:
Moje rozwiazanie jest poprawne, poniewaz opiera sie na prostej idei algorytmu dynamicznego, ktora jest dobrze znana.
Szacowana złożoność obliczeniowa:
Zlozonosc programu szacuje na O(n^2), poniewaz w pesymistycznym wariancie bede liniowo przegladal wszystkie opcje dla kazdego
z obiektow, ktore rowniez przegladam w linowym czasie'''
from zad9testy import runtests

def min_cost(O,C,T,L):
    n=len(O)
    Parkingi=[(i,i) for i in range(n+2)]
    for i in range(n):
        Parkingi[i]=(O[i],C[i])                     #Pierwsze jest polozenie parkingu od miasta A, a drugie jest jego cena
    Parkingi[n]=(0,0)
    Parkingi[n+1]=(L,0)
    n+=2
    Parkingi.sort(key=lambda x:x[0])
    Wynik=[[float('inf') for i in range(2)] for j in range(n)]
    Wynik[0][0]=Wynik[0][1]=0
    for i in range(1,n):
        price=Parkingi[i][1]
        #Teraz liczymy wynik dla braku wyjatku Wynik[i][0]
        j=i-1
        temp=Wynik[j][0]
        while j>=0 and Parkingi[i][0]-Parkingi[j][0]<=T:
            if Wynik[j][0]<temp:
                temp=Wynik[j][0]
            j-=1
        Wynik[i][0]=temp+price
        #Teraz liczymy wynik dla wyjatku Wynik[i][1]
        j,k=i-1,i-1
        temp=Wynik[j][0]
        while j>=0 and Parkingi[i][0]-Parkingi[j][0]<=2*T:
            if Wynik[j][0]<temp:
                temp=Wynik[j][0]
            j-=1
        while k>=0 and Parkingi[i][0]-Parkingi[k][0]<=T:
            if Wynik[k][1]<temp:
                temp=Wynik[k][1]
            k-=1
        Wynik[i][1]=temp+price
    return Wynik[n-1][1]

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost,all_tests=True)