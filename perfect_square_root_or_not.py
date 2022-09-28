t=int(input())
c=0
for i in range(1,t):
    d=i
    if((t/i)==d):
        c=1
if(c==1):
    print("True")
else:
    print("False")
