class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        maxl = 0
        for r in range(len(s)):
            count[s[r]]  = count.get(s[r] , 0) + 1
            #max(count) = will give the char 
            # validwindow = (r-l+1) - max(count.values()) 
            # while validwindow <= k:  while shrinks too aggressively
            while (r-l+1) - max(count.values())  > k: 
                #decrement the count of that character
                count[s[l]]-=1
                l+=1
            maxl = max(maxl , r-l+1)
        return maxl
        