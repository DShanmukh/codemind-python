n=int(input())
c=0
c1=0
for i in range(1,n+1):
    if(n%i==0):
        c=0
        if i == 1:
            c=3
        for j in range(1,n+1):
            if(i%j==0):
                c+=1
        if(c>2):
            c1+=1
print(c1)