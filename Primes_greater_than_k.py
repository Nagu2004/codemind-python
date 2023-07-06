def prime(n):
    c=0
    if n==1:
        return False
    else:
        for i in range(1,n+1):
            if n%i==0:
                c+=1
        if c==2:
            return True 
        else:
            return False
n=int(input())
l=list(map(int,input().split()))
k=int(input())
x=0
for i in l:
    if i>=k:
        if prime(i)==True:
            x+=1
print(x)