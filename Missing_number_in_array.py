t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=sum(l)
    p=(n*(n+1))//2
    print(p-k)