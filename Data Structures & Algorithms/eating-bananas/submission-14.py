class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        # hours = 0
        res = r
        while l<=r:
            hours = 0
            m = (l+r)//2
            # print("mm" , m)
            for p in piles:
                # print(p)
                hours+= math.ceil(p/m)
            # print(hours)
            # print(m)
                #if it is valid
            if hours<=h:  
                #aain it should have been m , not r 
                
                r = m - 1
                res = min(m, res) 
                # print("here" , res)
                # print
                #this shoulf be bfefor edecrementing
                # res = min(r , res)
            else:
                l = m + 1

        return res