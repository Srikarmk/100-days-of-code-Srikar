inp=[0,1,1,2,3,5,8]
n=len(inp)-2
l=[]
a,b=0,1
l.append(a)
l.append(b)
while n!=0:
    c=a+b
    a,b=b,c
    l.append(c)
    n-=1
if l==inp:
    print("Yes it is a fib seq")
else:
    print("No not a fib seq")

# int(input("Enter how many terms of fibonnaci sequence you want to generate : "))