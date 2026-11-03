class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n+1)}

        for u , v , w in times:
            adj[u].append([w , v])

        print(adj)

        minheap = [[0 , k]]

        #dist , dst

        visited = set()

        t = 0

        while minheap:
            dist , node = heapq.heappop(minheap)

            if node in visited:
                continue

            visited.add(node)

            t = max(t , dist)
            
            for dist2 , n2 in adj[node]:
                if n2 not in visited:
                    heapq.heappush(minheap , [dist+dist2 , n2])
                
            
        return t if len(visited) == n else -1