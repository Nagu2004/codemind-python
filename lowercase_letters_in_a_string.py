s=input()
l=[i for i in range(97,123)]
c=0
for i in s:
    if ord(i) in l:
        c+=1
print(c)