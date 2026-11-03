class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res+= self.countpali(s , i , i)
            res+=self.countpali(s , i , i+1)

        return res


    
    def countpali(self ,input_s, l , r):
        res = 0
        while l >=0 and r <len(input_s) and input_s[l] == input_s[r]:
            res+=1
            l-=1
            r+=1
        return res
        

        