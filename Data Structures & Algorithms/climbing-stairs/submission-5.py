class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}

        def dfs(i):
            #if we reach the top stairs
            if i==n:
                return 1
            if i>n:
                return 0

            
            if i in dp:
                return dp[i]

            #dp[i+1] ,[i+2]
            #n. =2 , i = 0 dfs(2) = 1 , dfs

            dp[i] = dfs(i+1) + dfs(i+2)

            return dp[i]

        #- - - - 
        return dfs(0)

        # one = 1
        # two = 1
        # for i in range(n-2 , -1 , -1):
        #     temp = one+two
        #     one = two
        #     two = temp

        # return two




        