n=int(input())
l=[int(x) for x in input().split()]
k=[]
k1=[]
for i in range(n):
    if(l[i]==0):
        k.append(l[i])
    else:
        k1.append(l[i])
print(*(k1+k))