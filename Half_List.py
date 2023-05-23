n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(n-1,n//2-1,-1):
    c.append(l[i])
for j in range(0,n//2,1):
    c.append(l[j])
for k in c:
    print(k,end=" ")