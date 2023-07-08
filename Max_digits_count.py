def dc(n=[]):
    k=[]
    for i in n:
        c=0
        while i>0:
            r=i%10
            c+=1
            i=i//10
        k.append(c)
    return k
n=int(input())
l=list(map(int,input().split()))
for i in l:
    x=dc(l)
print(x.count(max(x)))
    

    