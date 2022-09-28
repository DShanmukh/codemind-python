a=int(input())
b=int(input())
sum=0
for i in range(1,b):
    if(a%i==0 and a!=i):
        sum=sum+i
        
if(sum==b):
    print("Amicable")
else:
    print("Not Amicable")
