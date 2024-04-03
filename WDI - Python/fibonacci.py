#Wypisanie n-tego elementu ciagu Fibonacciego iteracyjnie oraz rekurencyjnie wraz z porownaniem czasow
import time

def fib(n):
    a,b=0,1
    for i in range(1,n):
        c=a+b
        a=b
        b=c
    return a

def fib_rek(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_rek(n-2)+fib_rek(n-1)

n=40
mem=[0 for _ in range(n)]

def fib_rek_tab(n):
    global mem
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_rek_tab(n-2)+fib_rek_tab(n-1)

ft=time.process_time()
print("N-ty element ciagu Fibonacciego policzony iteracyjnie ",fib(n))
st=time.process_time()
print("N-ty element ciagu Fibonacciego policzony rekurencyjnie ",fib_rek(n))
tt=time.process_time()
print("N-ty element ciagu Fibonacciego policzony rekurencyjnie z tablicowaniem ",fib_rek_tab(n))
fh=time.process_time()
print("Czas iteracyjnego: ",st-ft,"Czas rekurencji: ",tt-st,"Czas rekurencji z tablicowaniem: ",fh-tt)

