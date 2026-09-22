class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding dynamic window

        # seen = set()
        # longest = 0
        # l = 0
        # for r in range(len(s)):
        #     # This is a classic amortized sliding-window analysis.

        #     # If l were reset back to 0 for every r, then yes, you could get O(n²). But here:
        #     while s[r] in seen:
        #         #remove the starting char , left most -> needs to be contingous
        #         seen.remove(s[l])
        #         # seen.replace will remove all the char occurunces
        #         l+=1
        #     seen.add(s[r])
        #     curr_length= r-l+1
        #     longest = max(longest , curr_length)

        # return longest


        # seen = set()

        # l = 0
        # maxl = 0

        # for r in range(len(s)):

        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l+=1
        #     seen.add(s[r])
        #     maxl = max(maxl , r-l+1)

        # return maxl




















        seen = set()
        l = 0

        r = 1
        
        longest = 0
        for r in range(len(s)):
            
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest = max(longest , r-l+1)

        return longest





            


        