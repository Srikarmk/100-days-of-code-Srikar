nums=[1,2,1]
n=len(nums)
ans=[]*(2*n)
print(ans)
for i in range(n):
    print(i)
    ans[i]=nums[i]
    ans[i+n]=nums[i]
print(ans)