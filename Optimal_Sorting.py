t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if a==b:
        print("0")
    else:
        print(max(a)-min(a))