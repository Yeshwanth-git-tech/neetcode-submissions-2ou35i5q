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

        minheap  = [[0 , 0]]
        #dist , 0th index points

        visited = set()

        res = 0

        while len(visited) < len(points):
            d , s = heapq.heappop(minheap)

            # if s not in visited:
            if s in visited:
                continue
            
            visited.add(s)

            res+=d

            for d2 , nei in adj[s]:
                if nei not in visited:
                    heapq.heappush(minheap ,[d2 , nei])

        return res

                