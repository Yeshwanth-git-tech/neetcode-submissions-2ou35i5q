class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r  = max(piles)
        res = r
        while l<=r:
            hours = 0
            k = (l+r)//2
            for p in piles:
                hours+=math.ceil(p/k)
            print(hours)
                #se you are doing this insiede for loop so each for each p 
                #that sikropng , after you calculate hours for ine iteration you have to get out 
                # if hours<=h:
                #     #we can still decrease
                #     r = k-1
                #     res = min(res , r)
                # else:
                #     l = k+1

            if hours<=h:
                r = k-1
                res = min(res , k)
            else:
                l = k+1

        return res




        