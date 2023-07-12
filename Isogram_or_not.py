s=input()
s=s.split()
k=''
for i in s:
    k+=i
if len(k)==len(set(k)):
    print(True)
else:
    print(False)