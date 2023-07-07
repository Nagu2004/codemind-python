def palin(n):
    s=str(n)
    t=int(s[::-1])
    if n==t:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if palin(i)==True:
        c+=1
print(c)