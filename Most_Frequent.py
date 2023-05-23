n=int(input())
a=list(map(int,input().split()))
m=-1
c=0
res=[]
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]==a[j]:
            c+=1
    if c>m:
        m=c
        res=a[i]
    elif c==m:
        if a[i]<res:
            res=a[i]
print(res)        