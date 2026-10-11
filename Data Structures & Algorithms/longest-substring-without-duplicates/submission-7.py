class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = set()
        longest = 0
        l = 0
        r = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            #we move r when window is valid
            longest = max(longest , r-l+1)
            r+=1
        return longest
            

        