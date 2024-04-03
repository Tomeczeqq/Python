import random
import time
import copy

'''n=int(input())
X=[0]*n
for i in range(n):
    X[i]=int(input())
print(quicksort_iter(X))'''

tab1=[random.randint(0,10**5) for i in range(100000)]
tab2=copy.deepcopy(tab1)
ft=time.process_time()
#quicksort(tab1,0,len(tab1)-1)
st=time.process_time()
#mergesort(tab2,0,len(tab2)-1)
tt=time.process_time()
print("Quicksort: ",st-ft,"Mergesort: ",tt-st)