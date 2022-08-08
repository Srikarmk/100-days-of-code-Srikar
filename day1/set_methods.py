names={"Naruto","Goku","Luffy","Zoro"}
names.update(["Midoriya","Tanjiro","Eren"])
print(names)
print(names.pop())
print(names)

shape={'circle','square','triangle','rectangle','rhombus'}
shape.add('Trapezium')
shape.remove('rhombus')  
shape.discard('cycle')
print(shape)
sp={1,2,3,4}
sp.clear()
print(sp)
del sp 
shape1={'circle','rhombus','ring'}
print(shape.union(shape1))
print(shape.intersection(shape1))
s=shape.intersection(shape1)
print(s.issubset(shape))
print(shape.issuperset(s))
print(shape.difference(shape1)) #returns shape items which are not in shape1 
print(shape.isdisjoint(shape1))




