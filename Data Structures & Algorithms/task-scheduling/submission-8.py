class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []    

        count = Counter(tasks)


        for cc, c in count.items():
            heapq.heappush(maxheap , -1*c)
        
        q = deque()

        t = 0
        while maxheap or q:
            t+=1
            if maxheap:
                c = heapq.heappop(maxheap)
                cnt = 1 + c

                if cnt:
                    q.append([cnt , t+n])
            if q and q[0][1] == t:
                c , tt = q.popleft()
                heapq.heappush(maxheap ,c)
            
        return t
        
