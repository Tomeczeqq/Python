#Zwraca sume wszystkich podzbiorow z podanego zbioru
def sum(T,start,iloczyn):
    result=0
    n=len(T)
    for i in range(start,n):
        result+=iloczyn * T[i]
        result+=sum(T,i+1,iloczyn * T[i])
    return result


T=[0,1,2,3]
print(sum(T,0,1))