n=int(input())
a=list(map(int,input().split()))
c1=0
c2=0
for i in range(0,n):
    if a[i]%2==0:
        c1+=1
    else:
        c2+=1
print(c1,c2)        
        