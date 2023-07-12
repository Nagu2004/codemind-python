a,b=map(int,input().split())
m=[]
e=0
o=0
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(a):
    for j in range(b):
        if m[i][j]%2==0:
           e+=m[i][j]
        else:
            o+=m[i][j]
print(e,o)