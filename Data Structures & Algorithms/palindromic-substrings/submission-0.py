class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res+= self.helper(s , i , i)
            res+= self.helper(s , i , i+1)
        return res

        
    
    def helper(self , inputs , l , r):
        res = 0
        while l>=0 and r<len(inputs) and inputs[l] == inputs[r]:
            res+=1
            l-=1
            r+=1
        return res
        