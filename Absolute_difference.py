n=int(input())
l=list(map(int,input().split()))
c=0
p=1
p1=1
for i in range(0,n):
    c=0
    if(l[i]==1):
        c=2
    for j in range(1,l[i]):
        if(l[i]%j == 0):
            c+=1
    if(c<2):
        p=p*l[i]
    else:
        p1=p1*l[i]
y=abs(p1-p)
print(y)
        
    