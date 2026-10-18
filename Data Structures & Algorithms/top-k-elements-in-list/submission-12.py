class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n , 0) + 1

        #so key , and value is frequency
        minheap = []
        for n, v in count.items():
            heapq.heappush(minheap , [v , n])

        while len(minheap) > k:
            heapq.heappop(minheap)
        res = []
        for v , n in minheap:
            res.append(n)

        return res
        
        