n=int(input())
l=list(map(int,input().split()))
c=0
c1=0
for i in range(n):
    tem=l[i]
    c=0
    while(tem!=0):
        r=tem%10
        c+=1
        tem=tem//10
    if(tem==0):
        if(c%2==0):
            c1+=1
print(c1)
        