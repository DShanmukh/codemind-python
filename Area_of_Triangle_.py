import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
e=math.sqrt(d)
print("%.2f"% round(e,2))