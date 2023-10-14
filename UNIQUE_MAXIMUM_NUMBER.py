n=int(input())
l=list(map(int,input().split()))
k=0
c=[]
for i in range(n):
    k=l.count(l[i])
    if(k==1):
        c.append(l[i])
if(len(c)>0):
    print(max(c))
else:
    print("-1")