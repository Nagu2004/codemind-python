def palin(n):
    s=str(n)
    t=int(s[::-1])
    if n==t:
        return True
    else:
        return False
n=int(input())
r=0
f=0
for i in range(n+1,10000):
    if palin(i)==True:
        f+=1
        break
    else:
        f+=1
for j in range(n-1,0,-1):
    if palin(j)==True:
        r+=1
        break
    else:
        r+=1
if f==r:
    print(j,i)
elif f>r:
    print(j)
else:
    print(i)

