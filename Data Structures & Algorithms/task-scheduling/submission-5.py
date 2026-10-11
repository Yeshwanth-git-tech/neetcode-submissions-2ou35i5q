class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        heap = [-i for i in counts.values()]

        heapq.heapify(heap)

        q = deque()

        time = 0
        while heap or q:
            time+=1
            if heap:
                #when we pop we complete the task so we decrement the count , 
                #here we have taken max heap , so 1+ , is decremtnb
                c = 1+heapq.heappop(heap)
                #this should be added to queue with time so that it can be ahgain pusjhed and the task can be completed
                if c:
                    q.append([c , time+n])
            
            if q and q[0][1] == time:
                c , t = q.popleft()
                heapq.heappush(heap , c)
        return time



