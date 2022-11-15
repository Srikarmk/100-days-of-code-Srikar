maxNum=int(input("Enter a number"))
nums=[]
for i in range(1,maxNum+1):
    if i%2!=0:
        nums.append(i)
print(nums)