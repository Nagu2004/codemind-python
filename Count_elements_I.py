a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(set(l1))
l4=list(set(l2))
s=[]
for i in range(len(l3)):
    for j in range(len(l4)):
        if l3[i]==l4[j]:
            s.append(l3[i])
print(len(s))