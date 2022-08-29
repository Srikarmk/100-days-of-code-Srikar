'''Higher order function  - is a func 
                            1. accept functions as args or 
                            2.Return functions

'''

#1 


def circle(r):
    return 3.14*(r**2)
def square(a):
    return a**2

def area(shape):    
    value=shape(int(input()))
    print(value)

shape=input('Enter c or s: ')
if shape=='c':
    area(circle)
else:
    area(square)

#2

def exp(a):
    def add(b):
        return a+b
    return add

e=exp(10)
x=e(20)
print(x)