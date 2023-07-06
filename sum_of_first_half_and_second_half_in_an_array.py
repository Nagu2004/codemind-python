n=int(input())
l=list(map(int,input().split()))
s=0
x=0
k=len(l)//2
for i in range(k):
    s+=l[i]
for i in range(k,len(l)):
    x+=l[i]
print(s)
print(x)
        