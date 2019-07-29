a,b=map(int,input().split())
z=list(map(str,input().split()[:a]))
c=sorted(z)
print(c[b-1])

