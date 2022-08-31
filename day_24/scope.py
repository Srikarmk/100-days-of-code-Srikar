# def func():
#     global x
#     x=10
#     print(x)

# x=2

# func()
# print(x)

from glob import glob


def func():
    sum=5
    def add():
        nonlocal sum
        sum=20+10
        print(sum)
    add()
    print(sum)
    print(locals())
    print(globals())    

global sum
sum=25
func()
print(sum)