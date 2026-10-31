class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}

        for char in s1:
            count[char] = count.get(char , 0) + 1


        print(count)
        print(len(count))
        need = len(count)
        have = 0
        window = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] not in window:
                window[s2[r]] = window.get(s2[r],0)+1
            else:
                window[s2[r]]+=1
            print(window)
            if s2[r] in count and count[s2[r]] == window[s2[r]]:
                have+=1
            # if len(count) == len(window):
            if r-l+1 == len(s1):
                if have == need:
                    # return s[l:r+1]
                    return True

                #if not matched
                if s2[l] in count and count[s2[l]] == window[s2[l]]:
                    have-=1
                window[s2[l]]-=1
                l+=1
        
            
        return False