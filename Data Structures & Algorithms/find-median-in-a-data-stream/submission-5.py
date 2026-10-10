class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        #so i will add the num to self.small maxheap

        heapq.heappush(self.small , -1*num)


        #is greater than large heap min then pop and push it over to large heap
        #book keeping if smal and large
        if (self.small and self.large) and (-1*self.small[0] > self.large[0]):
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large , val)

                #then check. the length of small heap it is greater than large heap pop and push the max value 
        #so now you check the larg of max heap and min of large heao , if it the max value in small heap
        if len(self.small) > len(self.large) + 1:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large , val)

        if len(self.large) > len(self.small) + 1:
            val = -1*heapq.heappop(self.large)
            heapq.heappush(self.small , val)
        
        #is greater than large heap min then pop and push it over to large heap
        

    def findMedian(self) -> float:
        # if lensmall > large , small pop else large pop , else add max of small heaop and min of large heaop that is pop of both and /2 for sam elkenght , that is even
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0])/2
        
        
        