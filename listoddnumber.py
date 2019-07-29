x,y=map(int,input().split())
z=list(map(int,input().split()[:x]))
if (z[y]%2!=0):
    print(z[y])
else:
    print(z[y-1])
