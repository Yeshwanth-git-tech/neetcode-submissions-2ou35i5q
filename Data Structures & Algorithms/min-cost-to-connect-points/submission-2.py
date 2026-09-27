class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1 , y1 = points[i]
            for j in range(i+1 , len(points)):
                x2 , y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist , j])
                adj[j].append([dist , i])
                #since it is undirected

        minheap = [[0 , 0]]
        #cost , point

        res = 0

        visited = set()

        while len(visited) < len(points):
            cost , point = heapq.heappop(minheap)
            # if (cost , point) in visited:
            if point in visited:
                continue
            visited.add(point)

            res +=cost

            for dist , neigh in adj[point]:
                if neigh not in visited:
                    heapq.heappush(minheap , [dist , neigh])

        return res
        
        