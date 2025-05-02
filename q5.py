l=[("Yug"),(),("Ronit"),("rudra"),[]]
for i in l:
    if(type(i)==tuple and (len(i)==0)):
        l.remove(i)
        print(l)
        break
else:
    print("No empty tuple found")