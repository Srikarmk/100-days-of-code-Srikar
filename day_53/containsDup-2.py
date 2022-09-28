class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        final=set() #hashset
        for i in nums:
            if i in final:
                return True
            final.add(i)
        return
