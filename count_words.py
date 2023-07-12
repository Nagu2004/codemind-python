s=input()
l=['a','e','i','o','u','A','E','I','O','U']
s=s.split()
c=0
for i in s:
    if i[0] in l and i[-1] not in l:
        c+=1
print(c)