class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxprofit = 0
        r = 1
        while r<len(prices):
            if prices[l] < prices[r]:
                curr = prices[r] - prices[l]
                maxprofit = max(curr , maxprofit)
            else:
                l = r
            r+=1

        return maxprofit
            



        