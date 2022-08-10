#normal function with arguments
def square(a):
    return('square',a)
def circle():
    print("circle")
square(3)
circle()
#higher order funtion
def shape(square,lst):
    print(square(lst))

shape(square,[1,2,3,4,5])

#lambda Function - function with var 
x=lambda x,y:x+y
print(x(2,3))


def dog():
    return 'Bow'

def cat():
    return 'Meow'

def animal(tp):
    if tp=='d':
        return dog 
    else:
        return cat

b=animal('d')
print(b())

def potato():
    return 'aloo'

def veg(t):
    return potato 

bx=veg(2)
print(bx())