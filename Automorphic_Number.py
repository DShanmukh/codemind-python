import math
n=int(input())
m=int(math.pow(n,2))
g=int(math.log10(n)+1)
k=int(math.pow(10,g))
l=int(m%k)
if(l==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

    