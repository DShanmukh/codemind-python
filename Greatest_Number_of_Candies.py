n=int(input())
l=list(map(int,input().split()))
m=int(input())
p=max(l)
for i in l:
    if i+m>=p:
        print("True",end=" ")
    else:
        print("False",end=" ")