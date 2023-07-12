s=input()
l1=[i for i in range(65,91)]
l2=[i for i in range(97,123)]
c=0
for i in s:
    if ord(i) not in l1 and ord(i) not in l2 and ord(i)!=32:
        c+=1
print(c)