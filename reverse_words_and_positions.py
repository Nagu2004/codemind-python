s=input()
s=s.split()
l=[]
for i in range(-1,-len(s)-1,-1):
    l.append(s[i][::-1])
print(*l)