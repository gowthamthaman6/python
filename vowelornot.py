str=input("")
list=["A","E","I","O","U","a","e","i","o","u"]
for i in str:
    if i in list:
        print("yes")
        break
else:
    print("no")
