class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        #max heap
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            #-6 , -4 so first is smaller than second
            if first < second:
                heapq.heappush(stones , first - second)
        
        return -stones[0] if stones else 0
