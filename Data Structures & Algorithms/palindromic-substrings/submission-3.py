class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = i
            r = i
            res+= self.helper(s , l , r)
            l = i
            r = i+1
            res+= self.helper(s , l , r)
        return res

        
    
    def helper(self , inputs , l , r):
        res = 0
        while l>=0 and r<len(inputs) and inputs[l] == inputs[r]:
            res+=1
            l-=1
            r+=1
        return res
        