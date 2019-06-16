def GCD(x,y):
    rem=x%y
    if(rem==0):
        return y
    else:
        return GCD(y,rem)

n,m=map(int,input().split())
print(GCD(n,m))
