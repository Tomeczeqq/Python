#Algorytm Euklidesa - liczenie Najwiekszego Wspolnego Dzielnika dwoch liczb calkowitych

a=int(input("a="))
b=int(input("b="))
while b>0:
    reszta=a%b
    a=b
    b=reszta
print("Najwiekszym wspolnym dzielnikiem liczb jest ",a)