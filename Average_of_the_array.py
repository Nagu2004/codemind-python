n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    c+=l[i]
avg=c/n
print("%.2f"%avg)
    
    
      