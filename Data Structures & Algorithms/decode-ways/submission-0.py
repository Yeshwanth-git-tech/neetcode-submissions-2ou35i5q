class Solution:
    def numDecodings(self, s: str) -> int:
        #so first two indioces of dp is 1 , 1 
        #[1 ,1 ] - for 0 digits and the 1st digit is only one way to decode
        ##base case
        if s[0] == "0":
            return 0
        dp = [1 ,1]

        for i , num in enumerate(s[1:] , 2):
            ways = 0
            #dont forget to keep it a string zero
            if num != "0":
                ways+=dp[i - 1]
            if 10 <= int(s[i-2] + num) <=26:
                ways+=dp[i-2]
            #add the calculated ways to the end of dp
            dp.append(ways)
        return dp[-1]


