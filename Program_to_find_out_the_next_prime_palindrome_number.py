#PRIME PALINDRONE
def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    else:
        return True 
def palin(n):
    t=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if t==s:
        return True 
    else:
        return False
n=int(input())
n=n+1
while (n)>0:
    if prime(n)==True and palin(n)==True:
        print(n)
        break
    else:
        n+=1

    