n=int(input())
l=list(map(int,input().split()))
if len(l)%2==0:
    print(*l)
else:
    print(*l,0)