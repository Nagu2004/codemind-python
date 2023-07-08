def digit(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l[i]>0:
        c+=digit(l[i])
    else:
        c+=l[i]
print(c)
        