num=int(input())
sum=0
for i in range(1,num+1):
    if num%i==0:
        sum=sum+i
print(sum)