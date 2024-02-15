n=int(input())
l=list(map(int,input().split()))
t=int(input())
for i in range(t%len(l)):
    l.insert(0,l[-1])
    l.pop()
print(*l)