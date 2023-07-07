l=list(map(int,input().split()))
l1=list(map(int,input().split()))
a=0
b=0
for i in range(len(l)):
    for j in range(len(l1)):
        if(i==j and l[i]>l1[j]):
            a+=1
        if(i==j and l[i]<l1[j]):
            b+=1
print(a,b,end=" ")