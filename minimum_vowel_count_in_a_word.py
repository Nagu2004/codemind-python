s=input()
s=s.split()
l=['a','e','i','o','u','A','E','I','O','U']
x=[]
for i in s:
    c=0
    for j in i:
        if j in l:
            c+=1
    x.append(c)
print(min(x))
