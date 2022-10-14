t=int(input())
sum=0
pro=1
while(t>0):
    r=t%10
    sum=sum+r
    pro=pro*r
    t=t//10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")