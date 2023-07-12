s=input()
l=['a','e','i','o','u']
for i in s:
    if i in l:
       l.remove(i)
if l==[]:
    print(0)
else:
    print(*l)