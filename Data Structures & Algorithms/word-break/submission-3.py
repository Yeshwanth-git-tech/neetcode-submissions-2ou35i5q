class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)

        dp[len(s)] = True
        # we were able to macth all the words in the word dict

        for i in range(len(s)-1 , -1 , -1):
            for w in wordDict:
                if ((i+len(w)) <= len(s) and s[i:i+len(w)] == w):
                    dp[i] = dp[i+len(w)]
                #so we have found a match and dp[i] is True and we move on to next index
                if dp[i]:
                    break

        return dp[0]

        #dp[8] = True
        #dp[7] = False
        #dp[6] = False
        #dp[5] = False
        #dp[4] = True
        #dp[3] = False
        #dp[2] = False
        #dp[1] = False
        #dp[0] = True

                
        