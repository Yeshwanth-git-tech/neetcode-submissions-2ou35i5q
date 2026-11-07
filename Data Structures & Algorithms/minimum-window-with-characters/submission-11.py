class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count = {}
        for i in t:
            count[i] = count.get(i , 0) + 1

        need = len(count)
        have = 0
        window = {}

        minlen = float("infinity")
        res = [-1 , -1]

        l = 0
        for r in range(len(s)):
            # if s[r] not in window:
            window[s[r]] = window.get(s[r] , 0) + 1
            # window[s[r]]+=1

            if s[r] in count and count[s[r]] == window[s[r]]:
                have+=1
            
            while have == need:
                # print("we found")
                if r-l+1 < minlen:
                    minlen = r-l+1
                    res = [l , r]
                    # print(minlen)
                    # res = s[l:r+1]
                    
                window[s[l]]-=1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have-=1
                l+=1
        a , b = res
        # print (a , b)
        return s[a:b+1] if minlen!=float("infinity") else ""