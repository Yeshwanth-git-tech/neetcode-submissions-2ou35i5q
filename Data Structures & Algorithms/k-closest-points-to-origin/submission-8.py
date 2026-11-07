class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x1 , y1 in points:
            dist = (x1*x1) + (y1*y1)
            heapq.heappush(maxheap , [-dist , x1 , y1])

            if len(maxheap) > k:
                heapq.heappop(maxheap)

        
        res = []
        for i in range(k):
            dist , x1 , y1 = heapq.heappop(maxheap)
            res.append([x1 , y1])

        return res