class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        count = Counter(hand)
        print(count)

        minheap = []

        for h in count:
            heapq.heappush(minheap , h)

        print(minheap)
        

        while minheap:
            first = minheap[0]
            for i in range(first , first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i] == 0:
                    if i!= minheap[0]:
                        return False
                    heapq.heappop(minheap)
            
        return True