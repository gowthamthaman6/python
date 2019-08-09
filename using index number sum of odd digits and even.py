x=input()
z=list(x)
l1=[]
l2=[]
for i in range(1,len(z),2):
    l1.append(z[i])
for i in range(0,len(z),2):
    l2.append(z[i])
print(l1)
print(l2)
