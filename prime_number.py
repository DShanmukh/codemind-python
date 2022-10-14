t=int(input())
flag=0
for i in range(2,t//2):
    if(t%i==0):
        flag+=1
if(flag==0):
    print("prime")
else:
    print("not a prime")