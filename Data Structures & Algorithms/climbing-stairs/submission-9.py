class Solution:
    def climbStairs(self, n: int) -> int:
        # one = 1
        # two = 1

        # for i in range(n-2 , -1 , -1):
        #     temp = one+two
        #     two = one
        #     one = temp
        
        # return one

        dp = {}

        def dfs(i):
            if i == n:
                return 1
            if i >=n:
                return 0
            
            if i in dp:
                return dp[i]

            dp[i] = dfs(i+1) + dfs(i+2)

            return dp[i]

        return dfs(0)