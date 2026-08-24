class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        #the conditon must be iot should pop until it is lesss than or equal to k , 
        #so use while condition
        # if len(self.minheap) > self.k:
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap , val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0]


    #so basically (n-k)(logn) , and add is logn , which is improvement compared to binary search logn to search , but to add it is O(n)

        
        
        
