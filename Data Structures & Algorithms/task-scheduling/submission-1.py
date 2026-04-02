class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [- c for c in count.values()]

        heapq.heapify(maxheap)

        time = 0
        q = deque()

        while maxheap or q:
            time+=1
            if maxheap:
            #the most occuring task
                cnt = heapq.heappop(maxheap) + 1
            
            #decrementing the time , so that one time the task is processed
                if cnt:
                    q.append([cnt , time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap , q.popleft()[0])
        return time

