class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currmax= 1
        currmin = 1
        for n in nums:
            temp = currmax * n
            #so we trach currmax and currmin of each position
            currmax = max(n , temp , currmin*n)
            currmin = min(n , temp , currmin*n)
            res = max(res , currmax)

        return res
        # res = nums[0]
        # for i in range(len(nums)):
        #     curr = 1
        #     for j in range(i, len(nums)):
        #         curr*=nums[j]
        #         res = max(res , curr)

        # return res

        # ##O(n^2)
                
        