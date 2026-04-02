class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones

        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
    
        while len(stones) >1:
            #heappop
            max1 = -heapq.heappop(stones)
            max2 = -heapq.heappop(stones)
            res = max1-max2
            heapq.heappush(stones , -res)
        return -stones[0] if stones else 0
        # ans = -heapq.heappop(stones)
        # return ans

        