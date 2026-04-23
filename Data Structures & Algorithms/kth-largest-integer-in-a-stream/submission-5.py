class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        #dont forget to heapify
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
        # print(self.minheap)
        

    def add(self, val: int) -> int:
        #add 
        heapq.heappush(self.minheap, val)
        #now what if the k < len(minheap)
        if len(self.minheap) > self.k:
            #we pop
            heapq.heappop(self.minheap)

        #so now we will have a min heap with lenght =k
        #and the min value will be the kth element to be returned
        #it will return a list as nums is a list
        # print(self.minheap[0])
        return self.minheap[0]

        
        
