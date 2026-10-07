class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo ={}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float("inf")
            #dont forget to update res
            res = float("inf")    
            if rem in memo:
                return memo[rem]
            for c in coins:
                res = min(res , 1 + dfs(rem - c))
            memo[rem] = res

            return memo[rem]

        return dfs(amount) if dfs(amount)!=float("inf") else -1
        # dp = [amount+1]*(amount+1)

        # dp[0] = 0

        # for a in range(1 , amount+1):
        #     for c in coins:
        #         if a-c >=0:
        #             dp[a] = min(dp[a] , 1 + dp[a-c])

        # return dp[amount] if dp[amount]!= amount+1 else -1

        
        