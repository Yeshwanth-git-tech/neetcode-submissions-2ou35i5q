class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n+1)}

        for u, v , w in times:
            adj[u].append([w , v])

        heap = [[0 , k]]

        visited = set()

        t = 0

        # while len(visited) < len(times):
        while heap:
            w , node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)

            t = max(w, t)

            for w2 , nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap , [w+w2 , nei])

        
        return t if len(visited) == n else -1






