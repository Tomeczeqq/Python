''' Tomasz Janeczko 414613
Opis rozwiazania: W moim rozwiazaniu zgodnie ze wskazowka wyliczam F[i][b], czyli minimalny koszt znalezienia sie na planecie i
majac b ton paliwa. Na poczatku dla planety A uzupelniam wartosci dla kazdej jednostki paliwa (musimy taka jednostke zatankowac
na stacji A). Nastepnie sprawdzam tez, czy mozna z tej planety A sie do jakies kolejnej planety teleportowac. Teraz mozemy zaczac
wyliczac dynamicznie nasz wynik. W tym celu  zauwazmy,ze musimy sprawdzac kazda planete, ktora jest oddalona o nie wiecej niz E-b
odleglosci wstecz (w.p.p. nie bylibysmy w stanie doleciec na te planete - na razie zakladam, ze nie tankuje na doleconej stacji).
Dla kazdej tej planety ustalam potrzebna ilosc paliwa aby doleciec na planete i z pozostala zawartoscia baku rowna b i z tego
wyliczam wynik dla aktualnej planety biorac minimalna wartosc z kazdej z wczesniejszych planet. Po wyliczeniu wyniku przechodze
jeszcze raz po wszystkich wartosciach paliwa dla mojej aktualnej planety i sprawdzam, czy zatankowanie na niej nie byloby
korzystniejsze (jesli tak to zmieniam wynik). Na sam koniec wykonuje analogiczna procedure teleportu, ktora sprawdza, czy oplaca
sie teleportowac na jakas nastepna planete. Moim wynikiem koncowym jest koszt dotarcia na planete B z paliwem rownym 0.
Poprawność rozwiazania: Moje rozwiazanie jest poprawne, poniewaz dla kazdej mozliwosci sprawdzam i wyliczam wynik bazujac na tym,
ze kazdy dotychczasowy wczesniej wyliczony wynik jest poprawny (zalozenie programowania dynamicznego). W moim zadaniu
uwzgledniam fakt, ze moze oplacac nam sie zatankowac na kazdej z dostepnych wczesniej stacji (lub tez na aktualnej).
Szacowana złożoność obliczeniowa: Moja zlozonosc obliczeniowa szacuje na O(n^2*E^2), poniewaz dla kazdej wartosci paliwa dla
kazdej planety wyliczenie wyniku w pesymistycznym przypadku moze byc sprawdzaniem we wszystkich planet wyniku dla kazdego
tankowania.'''
from egz1btesty import runtests

def planets(D,C,T,E):
    n=len(T)
    F=[[float('inf') for i in range(E+1)] for j in range(n)]
    for i in range(E+1):
        F[0][i]=i*C[0]
    #Dostepny teleport z poczatkowej planety A
    teleport,cena_tel=T[0][0],T[0][1]
    if teleport!=0:
        F[teleport][0]=cena_tel     #Bak musi byc pusty
    #Liczenie dynamiczne wyniku: F[i][j]-koszt dotarcia na i-ta planete majac w baku j paliwa
    for i in range(1,n):
        for b in range(E+1):
            max_odl,j=E-b,i-1
            while j>=0 and D[i]-D[j]<=max_odl:
                j-=1
            if D[i]-D[j]>max_odl:
                j+=1
            for x in range(j,i):    #Przechodzimy po kazdej planecie,z ktorej jestesmy w stanie dotrzec na planete i
                odl=D[i]-D[x]
                potrzebne_pal=b+odl
                for y in range(potrzebne_pal+1):
                    F[i][b]=min(F[i][b],F[x][y]+(potrzebne_pal-y)*C[x])
            for x in range(E+1):
                F[i][b]=min(F[i][b],F[i][x]+(b-x)*C[i])
        #Zajmujemy sie teleportem - dla planety na ktora mozemy sie teleportowac sprawdzamy czy sie oplaca
        teleport,cena_tel=T[i][0],T[i][1]
        if teleport!=i:
            F[teleport][0]=min(F[teleport][0],F[i][0]+cena_tel)   #Bak musi byc pusty
    return F[n-1][0]

#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets,all_tests=True)