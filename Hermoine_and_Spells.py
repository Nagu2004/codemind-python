a,b,c=map(int,input().split())
if a>b and a>c :
    if b>c:
        print(a+b)
    else:
        print(a+c)
elif b>a and b>c :
    if a>c:
        print(a+b)
    else:
        print(b+c)
else:
    if a>b:
        print(a+c)
    else:
        print(b+c)

