n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(len(l)-2):
    if l[i]%2==1 and l[i+2]%2==1:
        if l[i+1]%2==0:
            c+=1
print(c)