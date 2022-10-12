t=int(input())
sum=0
for i in range(1,t+1):
    sum=sum+(1/i)
print("%.2f"% round (sum,2))