n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in range(len(l)):
    if l[i]%2==1:
        o.append(l[i])
    else:
        e.append(l[i])
print(*o,*e)