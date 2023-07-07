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
f=0
if n>0:
    for i in range(1,n+1):
        if n%i==0:
            if prime(i)==True:
                if i<7:
                    f=0
                else:
                    f=1
                    break
    if f==0:
        print('Ugly Number')
    else:
        print('Not Ugly Number')
else:
    print('Not Ugly Number')
            
    
                