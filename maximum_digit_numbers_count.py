n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    k=len(str(i))
    m.append(k)
for i in l:
    if max(m)==len(str(i)):
        print(i,end=' ')
    