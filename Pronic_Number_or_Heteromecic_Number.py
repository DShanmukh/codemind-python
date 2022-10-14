n=int(input())
f=0
for i in range(1,n):
    d=i+1
    if((n/i)==d):
        f=1
if(f==1):
    print('YES')
else:
    print('NO')
