n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        l1.append(l[i]) 
if l1==[]:
    print(-1)
else:
    print(max(l1))
