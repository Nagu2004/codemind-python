n=int(input())
l=[]
while n>0:
    r=n%10
    l.append(r)
    n=n//10
l1=l[::-1]
for i in range(len(l1)):
    if l1[i]==6:
        l1[i]=9
        break
for i in range(len(l1)):
    print(l1[i],end='')