class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = 0
        ans = ""
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > res:
                    res = r-l+1
                    ans = s[l:r+1]
                l-=1
                r+=1
            l = i
            r = i+1
            while l>=0 and r< len(s) and s[l] == s[r]:
                if r-l+1 > res:
                    res = r-l+1
                    ans = s[l:r+1]
                l-=1
                r+=1

        return ans

        


                    

        # res = 0
        # result = []
        # for i in range(len(s)):
        #     currlen = 0

        #     for j in range(i , len(s)):
        #         sub = s[i:j+1]
        #         if sub == sub[::-1] and len(sub) > res:
        #             res = len(sub)
        #             ans = sub

        # return ans
                    # currlen = j-i+1
                    # if currlen > res:
                    #     res = currlen
                    #     ans =s[i:j+1]
                    #     result.append(ans)

        # return "".join(max(result))

#         max picks "z" because "z" > "b" alphabetically
# Correct answer is "bab"

            
                

        