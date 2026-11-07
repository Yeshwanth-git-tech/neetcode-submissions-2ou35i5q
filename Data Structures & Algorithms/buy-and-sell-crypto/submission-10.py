class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxp = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                curr = prices[r]-prices[l]
                maxp = max(maxp , curr)
            else:
                l = r
        
        return maxp
