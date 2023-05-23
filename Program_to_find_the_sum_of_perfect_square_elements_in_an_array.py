n=int(input())
a=list(map(int,input().split()))
sum=0
pro=1
for i in range(0,n):
    pro=1
    while pro*pro<=a[i]:
        if pro*pro==a[i]:
            sum+=a[i]
        pro+=1
print(sum)        