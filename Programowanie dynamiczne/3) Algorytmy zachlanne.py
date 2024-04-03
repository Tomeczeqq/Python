'''Algorytmy zachlanne -> podejmij najlepsza lokalna decyzje i miej nadzieje, ze to zadziala:
- czesto bardzo szybkie
- czasem daja dobre rozwiazanie przyblizone, a nawet moga dac optymalne'''
#1-sze zadanie: Problem wyboru zadan - wybranie jak najwiekszej ilosci niepokrywajacych sie przedzialow
def zadania(Przed):
    n=len(Przed)
    Przed.sort(key=lambda x: x[1])
    i,result=0,0
    while i<n:
        result+=1
        end=Przed[i][1]
        while i<n and end>Przed[i][0]:
            i+=1
    return result

Przed=[(0,1),(1.5,2.01),(2,3),(1,2)]
print(zadania(Przed))

#2-gie zadanie: Kody Huffmana - kody binarne z symbolow o roznej dlugosci, ktore sa bardziej optymalne niz te o rownej dlugosci
#Kod prefiksowy - kod zadnego symbolu nie jest prefiksem innego kodu
#Algorytm: 1)Wez dwa smybole x i y o najmniejszej czestosci 2)Polacz je w jeden symbol z o sumie czestosci x i y

#3-cie zadanie: Problem plecakowy ciagly (mozna brac fragmenty przedmiotow)
#Algorytm zachlanny: wbieramy przedmioty o najlpeszym stosunku ceny do wagi
def static_knapsack(W,P,B):
    n=len(W)
    Zysk=[-1 for i in range(n)]
    for i in range(n):
        Zysk[i]=(P[i]/W[i],W[i],P[i])
    Zysk.sort(reverse=True)
    i,result=0,0
    while i<n:
        if B>Zysk[i][1]:
            result+=Zysk[i][2]
            B-=Zysk[i][1]
        else:
            result+=B*Zysk[i][0]
            break
        i+=1
    return result

W=[2,3,4,5]
P=[3,4,5,6]
B=8
value=static_knapsack(W,P,B)
print("Ostateczna wartość plecaka dla problemu ciaglego:",value)