class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(len(nums)-2 , -1 , -1):
            for j in range(i+1 , len(nums)):
                # print(i , j)
                if nums[i] < nums[j]:
                    # dp[i] = 1 + dp[j]
                    # see you need to have the max of itself or else it willc ahnge ebveruytiem
                    dp[i] = max(dp[i] , 1 +dp[j])

                    # print(dp)
        # print(dp)
        return max(dp)
        