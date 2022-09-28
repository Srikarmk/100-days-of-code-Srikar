class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=0
        n=[]
        for i in range(len(nums)):
            if nums[i] not in n:
                n.append(nums[i])
            elif nums[i] in n:
                count+=1    
        if count>0:
            return True
        elif count==0 or count<0:
            return False
