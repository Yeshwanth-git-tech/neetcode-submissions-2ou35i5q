class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # dp = [amount+1]*(amount+1)
        dp = [0]*(amount+1)

        dp[0] = 1
        #1 ay to get the coinchange for zero , tbat is choosing no coins

        for c in coins:
            for a in range(1 , amount+1):
                if a-c>=0:
                    dp[a]+=dp[a-c]

        print(dp)

        return dp[amount] if dp[amount]!=0  else 0
        