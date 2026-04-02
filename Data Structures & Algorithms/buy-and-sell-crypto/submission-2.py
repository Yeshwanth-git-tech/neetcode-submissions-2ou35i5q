class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")

        maxp = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            maxp = max(maxp , profit)

        return maxp if maxp>0 else 0