def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True 
    else:
        return False
def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
if prime(n)==True:
    if prime(rev(n))==True:
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
