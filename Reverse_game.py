def palin(n):
    s=str(n)
    t=int(s[::-1])
    return t
n=int(input())
s=[]
l=list(map(int,input().split()))
for i in l:
    s.append(palin(i))
print(*s)
    