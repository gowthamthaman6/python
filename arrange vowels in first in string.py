a=input("")
b=['a','e','i','o','u','A','E','I','O','U']
c=[]
d=[]
for i in a:
    if i in b:
        c.append(i)
for i in a:
    if i not in b:
        d.append(i)
list=(c+d)
print("".join(list))

        
