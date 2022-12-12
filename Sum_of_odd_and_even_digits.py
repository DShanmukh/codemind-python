n=int(input())
l=list(map(int,input().split()))
esum=0
osum=0
for i in range(n):
    if(i%2==0):
        esum=esum+l[i]
    else:
        osum=osum+l[i]
di=esum-osum
if(di==0):
    print("YES")
else:
    print("NO")