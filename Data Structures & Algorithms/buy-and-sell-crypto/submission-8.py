class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxp = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                curr = prices[r] - prices[l]
                maxp =max(curr , maxp)
            else:
                l = r
            r+=1

        return maxp




        