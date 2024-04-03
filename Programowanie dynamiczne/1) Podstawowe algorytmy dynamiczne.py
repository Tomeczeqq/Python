'''Metody rozwiazania problemow dynamicznych:
1)Okreslenie funkcji, ktora obliczamy
2)Zapisanie funkcji w postaci rekurencyjnej
3)Implementacja poprawnego kodu'''
#1-sze zadanie: Liczenie w sposob dynamiczny n-tego wyrazu ciagu Fibonacciego
def fib(n):
    F=[1 for i in range(n+1)]
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]

n=213
print(n,"element ciagu Fibonacciego:",fib(n))

#2-gie zadanie: Liczenie najdluzszego (niekoniecznie spojnego) rosnacego podciagu
def ps(T,P,i):
    if P[i]!=-1:
        ps(T,P,P[i])
    print(T[i],end=' ')

def lis(T):
    n=len(T)
    F,P=[1 for i in range(n)],[-1 for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if T[j]<T[i] and F[j]+1>F[i]:
                F[i],P[i]=F[j]+1,j
    wynik,indeks=F[0],0
    for i in range(1,n):
        if F[i]>wynik:
            wynik,indeks=F[i],i
    print("Dlugosc najdluszego rosnacego podciagu wynosi:",wynik)
    print("Elementy najdluzszego rosnacego podciagu: ",end='')
    ps(T,P,indeks)

T=[2,1,4,3,7,5,2,7,8,3]
lis(T)

#3-cie zadanie: Problem imprezy firmowej - wybranie wierzcholkow o maksymalnej sumie, ktore nie sa polaczone krawedzia
#f(v) - wartosc najlepszej imprezy w poddrzewie zakorzenionym w v                           f(v)=max(v.fun+E g(ui),g(v))
#g(v) - wartosc najlepszej imprezy w poddrzewie zakorzenionym w v, o ile v nie idzie na te impreze          g(v)=E f(ui)
class Employee:
    def __init__(self,fun):
        self.emp=[]
        self.fun=fun
        self.f=-1
        self.g=-1
    def f(self,v):
        if v.f>=0:
            return v.f
        x=v.fun
        for ui in v.emp:
            x+=self.g(ui)
        y=self.g(v)
        v.f=max(x,y)
        return v.f
    def g(self,v):
        if v.g>=0:
            return v.g
        x=0
        for ui in v.emp:
            x+=self.f(ui)
        v.g=x
        return v.g