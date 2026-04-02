class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count , window = {} , {}

        for c in t :
            count[c] = count.get(c , 0)+1
        l = 0
        have , need = 0 , len(count)
        res = [-1,-1]
        reslen = float("infinity")
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch , 0)+1
            #now lets check whether we have all the char and count
            if ch in count and window[ch] == count[ch]:
                have+=1
                    #char count of that must be equal
                    
            while have == need:
                #if the char count equals
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                #now we need min
                #pop from left
                #just tring to find the min
                #reducing the count as we are going to increment l and shrink the window
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have-=1
                #have to increment outside the condition as if the count is reduce
                #then we will shrink the window and look for the count again
                l+=1
        l , r = res
        return s[l:r+1] if reslen!=float("infinity") else ""

               
            
