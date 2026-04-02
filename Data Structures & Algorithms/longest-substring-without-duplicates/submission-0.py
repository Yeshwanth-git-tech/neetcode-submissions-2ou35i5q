class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charset = set()
        #length to return
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                #By removing s[l], you are properly shrinking the window 
                # from the left and keeping the charset perfectly in sync 
                # with the characters inside the s[l:r+1] slice.
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res= max(res , r - l +1)
        return res
        