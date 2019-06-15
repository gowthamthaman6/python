n=int(input(""))
composite=0
for i in range(2,n):
    if(n%i==0):
        composite=1
        break
if composite==1:
    print("no")
else:
    print("yes")
