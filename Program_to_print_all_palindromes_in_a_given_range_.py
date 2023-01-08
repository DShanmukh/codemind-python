n=int(input())
m=int(input())
for i in range(n,m+1):
    k=i
    rev=0
    while(k!=0):
        r=k%10
        rev=rev*10+r
        k=k//10
    if(rev==i):
        print(i,end=" ")