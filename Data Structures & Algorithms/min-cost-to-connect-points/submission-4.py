class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjmap = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1 , y1  = points[i]
            for j in range(i+1 , len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                #undirected
                adjmap[i].append((dist , j))
                adjmap[j].append((dist , i))

        minheap = [[0 , 0]]

        res = 0

        visited = set()

        # while minheap:
        #early exit
        while len(visited) < len(points):
            dist1 , i = heapq.heappop(minheap)
            if i in visited:
                continue
            visited.add(i)
            res+=dist1
            for dist2 , i2 in adjmap[i]:
                if i2 not in visited:
                    heapq.heappush(minheap , [dist2 , i2])

        # return res if len(visited) == len(points) else -1
        return res


