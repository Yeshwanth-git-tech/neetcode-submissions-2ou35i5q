class Solution:
    def rob(self, nums: List[int]) -> int:
        #etiher we can rob two house and skip the one in iddle
        # rob1 = 0
        # rob2 = 0


        # for n in nums:
        #     temp = max(n + rob1 , rob2)
        #     rob1 = rob2
        #     rob2 = temp

        # return rob2

        dp = {}

        def dfs(i):
            if i >=len(nums):
                return 0

            if i in dp:
                return dp[i]
            # combined = dfs(i) + dfs(i+2)
            combined = nums[i] + dfs(i+2)
            skip = dfs(i+1)
            dp[i] = max(skip , combined)  

            return dp[i]
        return dfs(0)