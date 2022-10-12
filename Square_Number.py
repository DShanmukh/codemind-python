t=int(input())
count=0
for i in range(t):
    for j in range(t):
        if(t==((i*i)+(j*j))):
            count=1
if(count==1):
    print("True")
else:
    print("False")