n=int(input())
if n>=3:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
    c=n-1
    for i in range(1,c+1):
        for j in range(i,c+1):
            print("*",end="")
        print()
else:
    print("The pattern is not possible")