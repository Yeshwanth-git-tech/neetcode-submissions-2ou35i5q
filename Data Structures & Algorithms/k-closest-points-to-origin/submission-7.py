class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        maxheap = []
        for x1 , y1 in points:
            dist = x1*x1 + y1*y1
            heapq.heappush(maxheap , [-1*dist , x1 , y1])
        
        while len(maxheap) > k:
            heapq.heappop(maxheap)

        print(maxheap)
        for dist , x , y in maxheap:
            res.append([x, y])
        return res