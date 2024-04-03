#1)Problem stacji benzynowych - jedzie z punktu A do punktu B spalajac 1 litr paliwa na jeden kilometr trasy z L litrowym bakiem
#1 przypadek - laczna liczba tankowan ma byc minimalna
def stacje_1(L,S):
    n=len(S)
    pos,result=0,0
    while pos<n:
        i=pos
        while i>=pos-L and S[i] is None:
            i-=1
        result+=1
        pos+=L-(pos-i)
    return result

#2 przypadek - koszt przejazdu ma byc minimalny (kazda stacja ma dowolna cene za litr) i mozemy tankowac dowolna ilosc paliwa
def stacje_2(L,S):
    n=len(S)
    pos,petrol,result=0,0,0
    while pos<n:
        #1-szy indeks to pozycja stacji, zas 2-gi indeks to cena paliwa na tej stacji
        cheapest_station=sorted([x for x in enumerate(S)[pos:pos+L] if x[1]],key=lambda x: x[1])[0]
        if cheapest_station[0]==pos:                #Obecnie jestesmy na najtanszej stacji - tankujemy do pelna paliwo
            refuelling=min(L-pos,n-pos-petrol)
            petrol+=refuelling
            result+=refuelling*cheapest_station[1]
            pos+=min(L,n-pos)
        else:                                       #Idziemy do tanszej stacji z idealnie zatankowanym bakiem
            distance=cheapest_station[0]-pos
            part_refuelling=max(0,distance-petrol)
            petrol+=part_refuelling
            result+=part_refuelling*S[pos]
            pos+=distance
    return result

#3 przypadek - koszt przejazdu ma byc minimalny, ale jesli tankujemy, to musimy zrobic to do pelna - NIE ISTNIEJE ZACHLAN

#2)Pokrycie przedzialami jednostkowymi - ile trzeba wziac przedzialow o dlugosci 1 tak aby pokryc wszystkie punkty
def przedzialy_reverse(P):
    P.sort(reverse=True)
    result=0
    while P:
        beginning=P[-1]
        while beginning<=P[-1]<=beginning+1:
            P.pop()
        result+=1
    return result

#3)Wybor zadan z terminami - dany zbior zadan T={t1,...tn} z terminami wykonania d(ti) o zysku g(ti) i zwrocic podzbior zadan,
#ktore da najwiekszy zysk; wykonanie kazdego zadania trwa jednostke czasu (pierwsze zad wykonywane jest w chwili 0)
#Idziemy od konca ostatniego deadline i bierzemy zadanie o aktualnie najwiekszym zysku

#4)Ladowanie przyczep - jest n ladunkow o masach bedacych potegami dwojki i pojemnosc K przyczepy
#Nalezy zapelnic jak najbardziej przyczepe jednoczesnie wybierajac jak najmniej ladunkow
#Mozna brac po kolei od najwiekszych kazdy taki, ktory sie miesci (przez wlasnosc dwojki wiemy, ze bedzie to optymalne)