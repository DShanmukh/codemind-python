n= int(input())
if n>0:
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n//=10
    print(rev)
if n<0:
    y=abs(n)
    rev1=0
    while y!=0:
        r1=y%10
        rev1=rev1*10+r1
        y//=10
    h=rev1*(-1)
    print(h)