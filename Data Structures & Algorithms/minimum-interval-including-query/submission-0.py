class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        minheap = []
        # queries.sort() sorts the list in place , so the original order is lost

        # queries.sort() so when we loop through
        res = {}
        i = 0
        # for q in queries:
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <=q:
                l , r = intervals[i]
                heapq.heappush(minheap , (r-l+1 , r))
                #dont forget to increment
                i+=1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            
            res[q] = minheap[0][0] if minheap else -1

        return [res[q] for q in queries]


            # if minheap:
            #     res[q] = minheap[0][0]
            # else:
            #     res[q] = -1

            # res[q] = minheap[0][0] if minheap else -1