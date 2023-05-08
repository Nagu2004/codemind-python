n=int(input())
l=list(map(int,input().split()))
e=int(input())
for i in range(len(l)):
    if l[i]==e:
        print(True)
        break
else:
    print(False)
        