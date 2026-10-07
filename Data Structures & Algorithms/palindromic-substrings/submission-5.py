class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i , len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    res+=1

        return res
    #     #odd 
    #     res = 0
    #     for i in range(len(s)):
    #         #odd
    #         res+=self.countpali(i , i , s)
    #         #even
    #         res+=self.countpali(i , i+1 , s)

    #     return res

    # def countpali(self , l , r ,s):
    #     res = 0
    #     # for i in range(len(s)):
    #     #     l = r = i
    #     while l>=0 and r<len(s) and s[l] == s[r]:
    #         res+=1
    #         l-=1
    #         r+=1

    #     return res

    

        