class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        maxl = 0
        for r in range(len(s)):
            count[s[r]]  = count.get(s[r] , 0) + 1
            #max(count) = will give the char 
            # validwindow = (r-l+1) - max(count.values()) 
            # while validwindow <= k:  while shrinks too aggressively
            print(count)
            print("r" , r )
            print("l" , l)
            print("ww" , r-l+1)
            while (r-l+1) - max(count.values())  > k: 
                #decrement the count of that character
                count[s[l]]-=1
                l+=1
            
            maxl = max(maxl , r-l+1)
        return maxl

# r=0: count={'A':1}, (1-1)=0<=1 ✓, maxl=1
# r=1: count={'A':2}, (2-2)=0<=1 ✓, maxl=2
# r=2: count={'A':3}, (3-3)=0<=1 ✓, maxl=3
# r=3: count={'A':3,'B':1}, (4-3)=1<=1 ✓, maxl=4
# r=4: count={'A':4,'B':1}, (5-4)=1<=1 ✓, maxl=5
# r=5: count={'A':4,'B':2}, (6-4)=2>1 ✗
#      shrink! remove s[0]='A' → count={'A':3,'B':2}, l=1
#      (6-3)=3>1 ✗
#      shrink! remove s[1]='A' → count={'A':2,'B':2}, l=2
#      (5-2)=3>1 ✗  wait...
#      window = r-l+1 = 5-2+1 = 4
#      (4-2)=2>1 ✗
#      shrink! remove s[2]='A' → count={'A':1,'B':2}, l=3
#      window = 5-3+1 = 3
#      (3-2)=1<=1 ✓ maxl stays 5
# r=6: count={'A':1,'B':3}, (4-3)=1<=1 ✓
#      window = 6-3+1 = 4, maxl stays 5
        