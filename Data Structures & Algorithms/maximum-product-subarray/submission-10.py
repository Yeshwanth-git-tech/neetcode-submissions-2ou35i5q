class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currmax = 1
        currmin = 1
        #2 , 8 , 
        #temp = 8*-2 = -24
        #currmax = max(8 , -24 , -24) so here currmax should become 0 , 
        
        #min  = -24
        #res = max(8 , 8) = 8

        
        for n in nums:
            temp = currmax*n
            # currmax = max(res , temp , currmin*n)
            # currmin =  min(res , temp , currmin*n)
            currmax = max(n , temp , currmin*n)
            currmin = min(n , temp , currmin*n)
            res = max(res , currmax)

        return res
        