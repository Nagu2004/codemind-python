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
a=int(input())
b=int(input())
c=a+b
s=c+1
while s>0:
    if prime(s)==True:
        break
    else:
        s+=1
print(s-c)