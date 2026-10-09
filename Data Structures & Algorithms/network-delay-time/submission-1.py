class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjmap = {i:[] for i in range(1, n+1)}

        for u,v,w in times:
            # adjmap[u].append(w)
            # adjmap[u].append(v)
            adjmap[u].append((w,v))



        minheap = [[0 , k]]
        t = 0
        visited = set()
        while minheap:
            w1 , n1 = heapq.heappop(minheap)
            if n1 in visited:
                # return False
                continue
            
            visited.add(n1)

            t = max(t , w1)    
            for w2 , n2 in adjmap[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap , [w1+w2 , n2])

        return t if len(visited) == n else -1





