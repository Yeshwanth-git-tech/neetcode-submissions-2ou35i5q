"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda i:i.start)
        #start list
        #end list sorted 

        #so basically we will compare the start [0] and end[0] , since start comes from first , it will end first
        # so start : [0 , 5 , 10] end : [10 , 15 , 30]
        #first compare the start[0] and end[0] start[0] < end[0] - so start a new room and increment count and increment the index in start
        #now compare the next and enxt like that we will reach 10 in start which is == end 10 , so now close that room in end , so decrement count 
        #so now we reached the end of the start , now compare start 10 and end 15 , now 10 < 15 , so count+=1 and there is no ekement elft isn count , starrt tot decrment in end
        #return count 

        ##this is using two pointer


        ##using min heap it is same time complexity and space -O(nlogn) and O(n)

        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])

        # res , count = 0 , 0
        # s , e = 0 , 0

        # while s < len(intervals):
        #     if start[s] < end[e]:
        #         s+=1
        #         count+=1
        #     else:
        #         e+=1
        #         count-=1
        #     #result should be updated after both the conditions    
        #     res = max(res , count)
        
        # return res

        #minheap

        # minheap = []

        # for i in intervals:
        #     #the end is less than the next start
        #     if minheap and minheap[0] <= i.start:
        #         heapq.heappop(minheap)
        #     heapq.heappush(minheap , i.end)
        # return len(minheap)


        # intervals.sort(key = lambda i:i.start)

        # start = sorted([i.start for i in intervals])

        # end = sorted([i.end for i in intervals])

        # res , count = 0 , 0

        # #res to store the max value , and count to increment and decrement the rooms

        # s , e = 0 , 0

        # #so start will be the first to reach the len of intervals , so we will use that
        # while s < len(intervals):
        #     if start[s] < end[e]:
        #         s+=1
        #         count+=1
        #     else:
        #         e+=1
        #         count-=1
        #     res= max(res , count )

        # return res


        minheap = []
# for start , end in intervals:
#         ^^^^^^^^^^^
# TypeError: cannot unpack non-iterable Interval object

#         for start , end in intervals:
        for i in intervals:
            if minheap and minheap[0] <= i.start:
                heapq.heappop(minheap)
            #push 40 , push 10 , pop 10 , push 20
            heapq.heappush(minheap , i.end)

        return len(minheap)
                





















        