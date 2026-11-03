class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i , currsum):
            if i >=len(nums):
                return 1 if currsum == target else 0

            if (i , currsum) in dp:
                return dp[(i , currsum)]

            dp[(i , currsum)] = dfs(i+1 , currsum + nums[i]) + dfs(i+1 , currsum - nums[i])

            return dp[(i , currsum)]

        return dfs(0 , 0)
