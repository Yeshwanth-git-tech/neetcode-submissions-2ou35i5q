class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("infinity") ] * n
        prices[src] = 0

        for i in range(k+1):
            tmpprices = list(prices)
            for s , d , p in flights:
                #if the source can not be reached
                if prices[s] == float("infinity"):
                    continue
                if prices[s] + p < tmpprices[d]:
                    #prices[s] + p is to reach d
                    tmpprices[d] = prices[s] + p

            prices = tmpprices

        return -1 if prices[dst] == float("infinity") else prices[dst]
        