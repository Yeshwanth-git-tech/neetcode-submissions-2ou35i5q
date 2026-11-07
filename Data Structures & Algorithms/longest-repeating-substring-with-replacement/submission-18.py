class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #so the main logic is maxf of the coutn - windlwolenght > k:shrink the winow 

        count = {}

        l = 0

        longest = 0

        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = count.get(s[r] , 0) + 1
            else:
                count[s[r]]+=1

            # print(count)

            maxf = max(count.values())
            # print(maxf)
            # print(r-l+1)
            # while maxf - r-l+1 > k:
            while r-l+1 - maxf > k:
                count[s[l]]-=1
                l+=1
            # print(longest)
            longest = max(longest , r-l+1)

        return longest
            
