n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
c=0
for i in range(len(s)):
    if s[i]%2==1:
        c+=1
print(c)