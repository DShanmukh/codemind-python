n=int(input())
c=0
for i in range(0,10):
    f=0
    temp=n
    while(temp!=0):
        r=temp%10
        if(i==r):
            f+=1
        temp=temp//10
    if(f>1):
        c+=1
if(c==0):
    print("Unique Number")
else:
    print("Not Unique Number")