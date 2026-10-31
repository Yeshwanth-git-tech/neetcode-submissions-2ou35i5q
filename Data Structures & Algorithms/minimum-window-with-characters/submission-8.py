class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count = {}

        for char in t:
            count[char] = count.get(char , 0) + 1

        need = len(count)
        have = 0
        window = {}
        l = 0
        reslen = float("infinity")
        res = [-1 , -1]
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in count and count[s[r]] == window[s[r]]:
                have+=1

            while have == need:
                
                # if r-l+1 == len(t):
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l , r]


                window[s[l]]-=1
                #if not matched
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have-=1
                l+=1
        
        l , r = res
        return s[l:r+1] if reslen!=float("infinity") else ""