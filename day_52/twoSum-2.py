class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp={}
        for i ,n in enumerate(nums):
            diff=target-n
            if diff in mapp:
                return [mapp[diff],i]
            mapp[n]=i
        return
