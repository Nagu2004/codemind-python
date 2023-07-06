n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
for i in l:
    if i>=a and i<=b:
        l1.append(i)
if l1==[]:
    print(-1)
else:
    print(*l1)
        