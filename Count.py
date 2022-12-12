n=int(input())
c=0
c1=0
l=list(map(int,input().split()))
for i in range(n):
    if(l[i]%2==0):
        c+=1
    else:
        c1+=1
print(c,c1)