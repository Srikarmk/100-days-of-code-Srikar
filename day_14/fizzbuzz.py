l=[]
for i in range(1,101):    
    if (i%3==0 and i%5==0):
        l.append("Fizzbuzz")      
    elif (i%3==0 and i%5!=0):
        l.append("Fizz")
    elif (i%3!=0 and i%5==0):
        l.append("Buzz")
    else:
          l.append(i)
print(l)
    