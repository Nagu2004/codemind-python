def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True 
    else:
        return False
n=int(input())
if prime(n)==True:
    while n>0:
        r=n%10
        if prime(r)==True:
            n=n//10
        else:
            break
    if n==0:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')
            
        