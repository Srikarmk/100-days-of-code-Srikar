class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if len(s)==len(t):
                if s.count(i)!=t.count(i):
                    return False
                    break 
            else:
                return False
                break
        return True
        
