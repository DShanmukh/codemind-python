n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    c=0
    for j in range(i,n):
        if(l[i]<l[j]):
            c=j-i
            break
    print(c ,end=" ")