n=int(input())
l=list(map(int,input().split()))
f=int(input())
c=0
for i in range(len(l)):
    if l[i]==f:
        c+=1
print(c)