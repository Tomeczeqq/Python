#Otwieranie plikow
#Pierwsza metoda
t={}
f=open("plik.txt","r")
for line in f:
    line=line.strip('\n').lower()
    for x in line:
        t.setdefault(x,0)
        t[x]+=1
f.close()

for x in t:
    print(x,t[x])

#Druga metoda
from collections import defaultdict
t2=defaultdict(int)
with open("plik.txt","r") as f:
    for line in f:
        line=line.strip('\n').lower()
        for x in line:
            t2[x]+=1

for x in t2:
    print(x,t2[x])
