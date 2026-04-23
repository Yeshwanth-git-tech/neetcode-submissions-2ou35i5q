import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distances = []
        # for point in points:
        #     x , y = point[0] , point[1]
        #     dst = x*x + y*y
        #     # distances.append([x,y,dst])
        #     hashmap[x,y] = dst
        #     #[(x, y), dst]
        # print(hashmap)
        minheap = []
        for x , y in points:
            dist = x*x +y*y
            minheap.append([dist, x, y])
            #heapq.heappush(minheap , (dist , [x,y]))
        # you dont need to mention heap with respect to dist 
        #it automatically heaos with that first value     
        heapq.heapify(minheap)
        res= []
        while k > 0:
            distance , x , y = heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res

# Building minheap list: O(n)
# heapq.heapify(minheap): O(n) 
# popping k times: k * O(log n)

# So total: O(n + k log n)
# Space: O(n) for the heap + O(k) for result.