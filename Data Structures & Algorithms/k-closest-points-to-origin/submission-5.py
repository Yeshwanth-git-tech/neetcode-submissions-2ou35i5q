class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x1 , y1 in points:
            dist = (x1**2)+(y1**2)
            heapq.heappush(minheap , [dist , x1 ,y1])
        res = []
        while k>0:
           dist , x1, y1 =  heapq.heappop(minheap)
           res.append([x1 , y1])
           k-=1
        return res


        