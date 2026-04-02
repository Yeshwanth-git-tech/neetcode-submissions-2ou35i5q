class Solution:
    def countBits(self, n: int) -> List[int]:

        # dp = [0] * n - see you have to give n+1

        dp = [0] * (n+1)

        dp[0] = 0
        offset = 1

        for i in range(1 , n+1):
            #this is super conditon offset , 1*2 =2 , 2*2 = 4
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
