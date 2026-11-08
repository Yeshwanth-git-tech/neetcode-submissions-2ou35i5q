class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = defaultdict(list)

        

        for i in range(len(points)):
            x1 , y1 = points[i]
            for j in range(i+1 , len(points)):
                x2 , y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)

                adj[i].append([dist , j])
                adj[j].append([dist , i])

        
        heap = [[0 , 0]]
        visited = set()
        res = 0
        while len(visited) < len(points):
            d , node = heapq.heappop(heap)

            

            if node in visited:
                continue

            #forgot to add visigt
            visited.add(node)

            res+=d
            
            for d2 , n2 in adj[node]:
                if n2 not in visited:
                    heapq.heappush(heap , [d2 , n2])

        return res 