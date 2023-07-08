n=input()
n=n.split()
l=[]
for i in range(-1,-len(n)-1,-1):
    l.append(n[i])
print(*l)
    