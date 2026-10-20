class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count = {}

        for w in s1:
            count[w] = count.get(w , 0)+1

        need = len(count)
        have = 0
        l = 0
        window = {}

        print(need)
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r] , 0)+1

            if s2[r] in count and count[s2[r]] == window[s2[r]]:
                have+=1
     
            # print(have)
            print(len(window))
            print(r-l+1)

            # if r-l+1 == len(count):
            if r-l+1 == len(s1):
                if have == need:
                    return True
                if s2[l] in count and window[s2[l]] == count[s2[l]]:
                    have-=1
                window[s2[l]]-=1
                l+=1
                
        return False
                


