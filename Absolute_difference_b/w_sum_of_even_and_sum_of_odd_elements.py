n=int(input())
l=list(map(int,input().split()))
e=o=0
for i in range(len(l)):
    if l[i]%2==0:
        e+=l[i]
    else:
        o+=l[i]
print(abs(e-o))
    