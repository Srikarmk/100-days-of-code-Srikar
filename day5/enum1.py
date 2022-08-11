l1=[1,2,3,4,5,4]
l2=[3,4,5,6,6]
for i in enumerate(l1):
    print(i)
x=zip(l1,l2)
print(list(x))