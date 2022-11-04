t=int(input())
sum=0
for i in range(1,t):
    if(t%i)==0:
        sum=sum+i
if(sum>t):
    print("True")
else:
    print("False")
        