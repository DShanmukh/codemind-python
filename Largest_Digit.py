n=int(input())
large=0
for i in range(n):
    r=n%10
    if(r>large):
        large=r
    n=n//10
print(large)