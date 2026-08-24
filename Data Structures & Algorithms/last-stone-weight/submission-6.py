class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            max1 = -heapq.heappop(stones)
            max2 = -heapq.heappop(stones)
            res = max1 - max2 
            heapq.heappush(stones , -res)

        print(stones)

        if stones[0]:
            return -stones[0]    
        else:
            return 0
        