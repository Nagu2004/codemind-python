n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    c+=l[i]
avg=c//n
for k in range(n):
    if avg==l[k]:
        print(True)
        break
else:
    print(False)