n=input()
n=n.split()
l=[]
for i in n:
    l.append(len(i))
print(max(l))