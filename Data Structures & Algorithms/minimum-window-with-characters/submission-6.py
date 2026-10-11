class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = {}
        count_t = {}

        for i in t:
            count_t[i] = count_t.get(i , 0) + 1

        have = 0
        need = len(count_t)

        l = 0 
        res = [-1, -1]
        reslen = float("infinity")

        for r in range(len(s)):
            window[s[r]] = window.get(s[r] , 0) + 1
            #so here you forgot to check the count of windows[s[r]] == count_t[s[r]]
            # if s[r] in count_t:
            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have+=1

            while have == need:
                if (r-l+1) < reslen:
                    res = [l , r]
                    reslen = r-l+1
                #shrink the window now
                window[s[l]]-=1
                #check if it is valid
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have-=1
                l+=1

        l , r = res
        return s[l:r+1] if reslen!=float("infinity") else ""

        