s=input()
a=input()
l=['a','e','i','o','u','A','E','I','O','U']
x=[]
if a in s:
    for i in range(len(s)):
        if a==s[i]:
            print(True)
            print(i)
            break
else:
    print(False)