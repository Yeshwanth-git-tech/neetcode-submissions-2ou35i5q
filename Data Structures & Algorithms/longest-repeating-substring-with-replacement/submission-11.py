class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_s = {}
        maxf = 0
        l = 0

        res = 0
        
        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r] , 0)+1
            # maxf = max(count_s.values())
            maxf = max(maxf , count_s[s[r]])

            while (r-l+1) - maxf > k:
                #then window is not valid
                count_s[s[l]]-=1
                l+=1

            res = max(res , (r-l+1))

        return res
        