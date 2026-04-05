class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-1 , -1 , -1):
            for j in range(i+1 , len(nums)):
                if nums[i] < nums[j]:
                    #not max(1 , dp[j] , which is i+1)
                    dp[i] = max(dp[i] , 1 + dp[j])
                #not required as it is already 1     
                # dp[i] = 1

        #each index will have the LIS    
        return max(dp)
            