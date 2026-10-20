class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        #this is a longest  , so winow when invalid we shrink
        count = {}
        longest = 0
        maxf = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r] , 0) + 1
            maxf = max(count.values())
            
            while r-l+1 - maxf > k:
                count[s[l]]-=1
                l+=1
            longest = max(longest , r-l+1)

        return longest
        

