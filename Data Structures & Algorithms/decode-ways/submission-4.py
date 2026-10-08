class Solution:
    def numDecodings(self, s: str) -> int:
        # one = 1
        # two = 0

        # for i in range(len(s)-1 , -1 , -1):
        #     if s[i] == "0":
        #         curr = 0
        #     else:
        #         curr = one
        #     #dont forget to include the bracket for the and condtion    
        #     # if (i+1) < len(s) and s[i] == "1" or s[i] == "2" and s[i+1] in "0123456":
        #     if (i+1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
        #         curr = curr+two
        #     two = one
        #     one = curr

        # return one

        dp = {len(s):1}


        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i+1)

            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in"0123456")):
                res+=dfs(i+2)

            dp[i] = res

            return dp[i]


        return dfs(0)
            

        