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
m=0
for i in range(1,a+1):
    if a%i==0:
        if prime(i)==False:
            m+=1
print(m)
        