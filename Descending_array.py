n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n-1):
    if l[i]<l[i+1]:
        s=1
        break
    else:
        s=0
if s==0:
    print('yes')
else:
    print('no')