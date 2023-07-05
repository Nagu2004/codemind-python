n=int(input())
l=list(map(int,input().split()))
f=c=0
for i in range(len(l)):
    if l[i]%2==0 and i%2==0:
        f+=1
    if l[i]%2==0:
        c+=1
if f==c:
    print('True')
else:
    print('False')
        