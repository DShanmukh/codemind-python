t=int(input())

for i in range(t):
    count=0
    a=int(input())
    for j in range(a):
        if(a==j*j):
            count+=1
    if(count==1):
        print("True")
    else:
        print("False")
