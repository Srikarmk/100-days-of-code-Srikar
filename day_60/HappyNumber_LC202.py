class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNum(n):
            total =0
            while n>0:
                t=n%10
                total+=t*t
                n=n//10
            return total 
        
        hashset=set()
        while n!=1 and n not in hashset:
            hashset.add(n)
            n=nextNum(n)
        return n==1
