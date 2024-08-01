n=int(input())
m=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(l)
ds=0
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            ds+=m[i][j]
print(ds)