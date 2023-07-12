a,b=map(int,input().split())
m=[]
c=0
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(a):
    for j in range(b):
        c+=m[i][j]
print(c)