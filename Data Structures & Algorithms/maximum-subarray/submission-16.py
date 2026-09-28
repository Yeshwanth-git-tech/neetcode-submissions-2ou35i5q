class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
     
        if len(nums) == 1:
            return maxsum
            
        res = 0    
        for i in range(len(nums)):
            res+=nums[i]
            maxsum = max(res , maxsum)
            if res<0:
                res = 0

        return maxsum     