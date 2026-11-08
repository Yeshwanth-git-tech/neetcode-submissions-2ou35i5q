class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        for i in range(len(s)):
            res+=self.counthelper(s , i , i)
            res+=self.counthelper(s , i , i+1)
        
        return res

    def counthelper(self , s , l , r):
        res = 0
        reslen = 0
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r-l+1>reslen:
                reslen = r-l+1
                res+=1
            l-=1
            r+=1
        return res