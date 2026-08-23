class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding dynamic window

        seen = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                #remove the starting char , left most -> needs to be contingous
                seen.remove(s[l])
                # seen.replace will remove all the char occurunces
                l+=1
            seen.add(s[r])
            curr_length= r-l+1
            longest = max(longest , curr_length)

        return longest






























        # # seen = ""
        # seen = set()
        # #{'a','b', 'c', .....}
        # l = 0
        # maxl = 0

        # for r in range(len(s)):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         #seen = seen.replace(s[l] , "") #replace will remove all the occurence
        #         l+=1
        #     seen.add(s[r])
        #     maxl = max(maxl , r-l+1)
        # return maxl


        # # print(len(s))
        # while r < len(s)-1:
        #     seen+=s[r]
        #     print(seen)
        #     maxl = max(maxl , len(seen))
        #     print(r)
        #     r+=1

        #if we do like this we miss out th elast elment before that 
        #     if s[r] in seen:
        #         seen = seen.replace(s[l] , "")
        #         l+=1
        # return maxl
        #         #so we do not repeat the character
        #         # maxl = max(maxl , len(seen))
            


            


        