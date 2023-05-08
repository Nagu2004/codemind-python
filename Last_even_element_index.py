n=int(input())
l=list(map(int,input().split()))
for i in range(-1,-n-1,-1):
    if l[i]%2==0:
        print(n+i)
        break