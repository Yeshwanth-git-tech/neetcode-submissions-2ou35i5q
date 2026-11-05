class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res+=n%2
            #move the bit oepration 
            n = n >> 1
        return res
        