n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(-1,-len(l)-1,-1):
    if l[i]==0:
        c+=1
        pass
    else:
        s=s+2**(c)
        c+=1
print(s)
        
    