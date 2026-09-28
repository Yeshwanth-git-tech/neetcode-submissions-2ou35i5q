class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False


        count = {}

        for h in hand:
            count[h] = count.get(h , 0)+1
            
        minheap = []

        for h in count:
            heapq.heappush(minheap , h)

        res = []
        while minheap:
            first = minheap[0]
            group = []
            for i in range(first , first+groupSize):
            # for i in range(first , groupSize+1):
                if i not in count:
                    return False
                count[i]-=1
                # group.append(i)
                if count[i] == 0:
                    if i!= minheap[0]:
                        return False
                    heapq.heappop(minheap)


            # res.append(group)

        return True

        # print(res)
            



        

