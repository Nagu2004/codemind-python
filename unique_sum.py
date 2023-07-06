n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
k=0
for i in range(len(s)):
    k+=s[i]
print(k)