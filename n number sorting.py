n=int(input())
a=list(map(int,input().split()[:n]))
b=(sorted(a))
print(*b,sep=" ")
