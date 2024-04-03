#Zamiana systemu dziesietnego na binarny
def to_binary(n):
    t=[]
    while n>0:
        t.append(n%2)
        n//=2
    t.reverse()
    print("Liczba dziesietna zapisana w systemie binarnym: ",end='')
    for x in t:
        print(x,end='')

to_binary(2137)

#Zamiana systemu binarnego na dziesietny
def to_decimal(n):
    result=0
    exponent=len(n)-1
    for x in n:
        if x=="1":
            result+=1*2**exponent
        exponent-=1
    print("\nLiczba binarna zapisana w systemie dziesietnym:",result)

to_decimal("100001011001")
