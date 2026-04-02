class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #time complexity is O(n) has heapigy is O(n) and pop and push
        #is O(logn) , here n= 26 , so log26 , so it is O(n) 
        #in some cases there is this idle time too long , if [A,A,A,A,A] 
        # si it will be O(n*m)
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        q = deque()
        time = 0

        while maxheap or q:
            time +=1
            if maxheap:
                #here adding 1 to subtract the frequenct and increment time
                #unit consumption
                cnt = 1 + heapq.heappop(maxheap)
                #if the frequencty of the aplhabet is not zero
                if cnt:
                    q.append([cnt , time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxheap , q.popleft()[0])

        return time
