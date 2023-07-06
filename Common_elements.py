a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            if l1[i] not in s:
                s.append(l1[i])
print(*s)