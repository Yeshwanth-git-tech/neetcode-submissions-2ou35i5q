class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price = float("inf")

        # maxp = 0

        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     profit = price - min_price
        #     maxp = max(maxp , profit)


        l = 0
        maxp = 0

        for r in range(1 , len(prices)):
            if prices[r]> prices[l]:
                profit = prices[r] - prices[l]
                maxp = max(maxp ,profit)
            else:
                l = r

        return maxp
