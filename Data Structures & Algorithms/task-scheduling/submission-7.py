class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for t in tasks:
            count[t] = count.get(t , 0) + 1

        q = deque()

        maxheap = []

        for c in count.values():
            #you will tupe error when we docmpare str , int while jbehappusj
            # heapq.heappush(maxheap , [-1*c , t])
            heapq.heappush(maxheap , -1*c)
    
        time = 0
        while maxheap or q:
            time+=1
            if maxheap:
                # c , t = heapq.heappop(maxheap)
                c = 1 + heapq.heappop(maxheap)

                # count = 1 + c

                if c:
                    q.append([c , time+n])

            if q and q[0][1] == time:
                c , tt = q.popleft()
              
                # heapq.heappush(maxheap , [-1*c , tt])
                #the value is already negatice
                # heapq.heappush(maxheap , [c , tt])
                heapq.heappush(maxheap , c)

            
        return time 