class Solution:
    def climbStairs(self, n: int) -> int:

        # dp = {}

        # def dfs(i):
        #     if i >=n:
        #         return 1

            
        #     if i in dp:
        #         return dp[i]

        #     #dp[i+1] ,[i+2]

        #     dp[i] = dfs(i+1) + dfs(i+2)

        #     return dp[i]

        #- - - - 
        # return dfs(0)

        one = 1
        two = 1
        for i in range(n-2 , -1 , -1):
            temp = one+two
            one = two
            two = temp

        return two




        