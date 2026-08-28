import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        # print("max" , max(piles))
        #this is for sure , that res can be the max pile number
        res = r
        # hours = 0
        while l<=r:
            #you ahve to declare hours inide the while , so that it get uodated for every cycle
            hours = 0

            k = (l+r)//2

            for p in piles:
                hours+=math.ceil(p/k)
                #so for2 , it will be correct , and we are updating the res first and then moving k , so it should work 
            if hours<=h:
                res = min(res , k)
                r = k - 1
            else:
                l = k + 1
 

        return res



