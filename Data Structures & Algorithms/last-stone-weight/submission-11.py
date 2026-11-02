class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap , -1*stone)
        
        while len(maxheap) > 1: 
            stone1 = -1*heapq.heappop(maxheap)
            stone2 = -1*heapq.heappop(maxheap)
            newstone = stone1 - stone2
            heapq.heappush(maxheap, -1*newstone)
        
        return -1*maxheap[0]