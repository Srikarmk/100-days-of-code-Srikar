#data structures

'''
Lists 
Tuples 
Sets 
Dictionary
'''

# animals=["Dog","Cat","Cow",2] #ordered , mutable , square brackets
# animals.append("Tiger")
# print(animals)

# animal=("Dog","Cat","Cow",2) #ordered , immutable , rounded , het
# del animal
# print(animal)

# car={"alto","datsun","bmw","hurcan"}  #unordered , mutable , flower , hete  
#duplicates are not allowed 
# print(car) 

# #hashvalues 

# a=[1,2,3,4,6,7,8,4,1]
# a=list(set(a))

# print(*a)  # unpacking operator

# #type casting
# a=int('3')
# print(type(a))

#dict  -> key value pairs 

# word - meaning
# key - value

# a=[{"name":"Srikar","age":20,"study_year":4},{"name":"Sneha","age":22,"study_year":4},{"name":"Random","age":25,"study_year":4}]

# for i in range(3):
#     print(a[i]['age'])


# name=input()
# age=int(input())
# college=input()

# string = f"My name is {name} and i am {age} years old. I study at {college}" #formatted or template
# print(string)

a=input("Enter your num ")
b=input("Second number ")


if a=='2' and b=='3':
    print("Yes")
else:
    print("No")