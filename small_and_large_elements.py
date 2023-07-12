s=input()
s=s.split()
for i in s:
    k=min(i)
    break
for i in s:
    h=max(s[-1])
    break
print(k,h)