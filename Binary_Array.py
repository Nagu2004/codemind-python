n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i==0 or i==1:
        pass
    else:
        print('False')
        break
else:
    print('True')
        