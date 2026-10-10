class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("infinity")]*n

        prices[src] = 0
        for i in range(k+1):
            temp_prices = list(prices)
            for s , d, p in flights:
                if prices[s] == float("infinity"):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p

            prices = temp_prices
            
        return prices[dst] if prices[dst]!= float("infinity") else -1 
        