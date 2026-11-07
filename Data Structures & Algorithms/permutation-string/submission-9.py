class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = {}

        for s in s1:
            count[s] = count.get(s , 0) + 1

        need = len(count)
        have = 0

        window = {}
        l = 0
        
        for r in range(len(s2)):
            if s2[r] not in window:
                window[s2[r]] = window.get(s2 , 0) + 1
            else:
                window[s2[r]]+=1
            
            if s2[r] in count and window[s2[r]] == count[s2[r]]:
                have+=1
            
            # if len(window) == len(s1):
            if (r-l+1) == len(s1):
                if have == need:
                    return True

                if s2[l] in count and count[s2[l]] == window[s2[l]]:
                    have-=1
                window[s2[l]]-=1
                l+=1
        return False
                    



