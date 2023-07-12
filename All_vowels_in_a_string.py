s=input()
l1=['a','e','i','o','u']
l2=['A','E','I','O','U']
x=[]
for i in s:
    if i in l1:
        l1.remove(i)
for i in s:
    if i in l2:
        l2.remove(i)
if l1==[] or l2==[]:
    print(True)
else:
    print(False)