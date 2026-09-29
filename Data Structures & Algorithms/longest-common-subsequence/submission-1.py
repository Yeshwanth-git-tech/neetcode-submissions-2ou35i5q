class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dpp=[]
        # for i in range(len(text1)+1):
        #     row = []
        #     for j in range(len(text2)+1):
        #         row.append(0)
        #     dpp.append(row)
        # print(dpp)

        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        # print(dp)

        for i in range(len(text1)-1 ,-1 ,-1):
            for j in range(len(text2)-1 ,-1 ,-1):
                if text1[i] == text2[j]:
                    # dont forget to add 1
                    dp[i][j] =1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])


        return dp[0][0]

        # for i in range(len(text1)):
        #     for j in range(len(text2))

