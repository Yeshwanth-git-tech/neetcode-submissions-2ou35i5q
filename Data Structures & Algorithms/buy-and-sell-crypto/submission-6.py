class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = 0
        # r = 1
        # max_profit = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         max_profit = max(profit , max_profit)
        #     else:
        #         l=r
        #     r+=1 
        # return max_profit


        min_price = float("inf")
        max_price = 0

        for p in prices:
            min_price = min(min_price, p)

            # min_price = min(min_price, p) runs before the profit calculation. Buying and selling on the same day gives profit 0, which is fine, and it removes the need for the else branch.

            max_price = max(max_price , p - min_price)

        return max_price



        ##maxloss
        #the max price you can buy
        # max_price = float("-inf")

        # max_loss = 0

        # for p in prices:
        #     maxprice = max(p , max_price)

        #     maxloss = min(maxloss , p - maxprice)

        # return maxloss
            




