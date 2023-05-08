def sd(n):
    t=n
    s=str(n)
    c=0
    while n>0:
        r=n%10
        if r>0:
            if t%r==0:
                n=n//10
                c+=1
            else:
                return False
        else:
            return False
            break
    if len(s)==c:
        return True
f=int(input())
l=int(input())
for i in range(f,l+1,1):
    if sd(i)==True:
        print(i,end=' ')
