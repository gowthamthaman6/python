n=int(input())
b=list(map(int,input().split()[:n]))
c=sorted(b)
if (len(c)%2!=0):
    print(b[n//2])
else:
    print(b[n//2])
