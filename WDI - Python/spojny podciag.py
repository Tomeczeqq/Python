#Zwraca najwieksza sume spojnego podciagu
def ssp(T):
    n=len(T)
    temp,result=0,0
    for i in range(n):
        temp+=T[i]
        if temp<0:
            temp=0
        if temp>result:
            result=temp
    print("Najwieksza suma spojnego podciagu wynosi: ",result)

T=[1,2,3,-4,23,-43,22,3,-1,2,-5,4]
ssp(T)