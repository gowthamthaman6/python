a=int(input())
b=int(input())
sum=0
for i in range(1,a+1):
    print(i,end="")
    if (b==i):
        for c in range(b+1):
            sum+=c
            
print(sum)
