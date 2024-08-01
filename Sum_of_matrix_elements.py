r=int(input())
c=int(input())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
s=0
for i in range(r):
    for j in range(c):
        s+=m[i][j]
print(s)