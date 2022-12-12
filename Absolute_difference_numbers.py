num,b=map(int,input().split())
temp=num
rev=0
rev2=0
g=10**b
p=num%g
while temp>0:
    r=temp%10
    rev=rev*10+r
    temp=temp//10
i=rev%g
while i!=0:
    r1=i%10
    rev2=rev2*10+r1
    i=i//10
dif=abs(rev2-p)
print(dif)
    