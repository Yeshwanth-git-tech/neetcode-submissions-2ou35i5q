class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        longest = 0
        count = {}
        for r in range(len(s)):
            # if s[r] not in count:
            count[s[r]] = count.get(s[r] , 0) + 1
            # count[s[r]]+=1
            maxf = max(count.values())
            while r-l+1 - maxf > k:
                count[s[l]]-=1
                l+=1
            longest = max(longest , r-l+1)
          

        return longest

