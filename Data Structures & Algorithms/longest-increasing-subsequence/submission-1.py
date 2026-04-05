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

        # so basically we are doing the same thing in Longest increasing sequence there we have
        # the length stored in the the dp list in the respective index with respect tot nuber 
        # and then return max(dp) 
        # here the same concept but we save the lenght and count in the dp hashmap
        # and check all the edge cases and
        # then again compare with global maxlenLIS and res and then return res
            