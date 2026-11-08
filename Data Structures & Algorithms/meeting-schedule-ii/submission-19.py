"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start = sorted(i.start for i in intervals)
        # end = sorted(i.end for i in intervals)

        # s = 0
        # e = 0

        # curr_rooms = 0
        # maxrooms = 0

        # while s<len(start):
        #     if start[s] < end[e]:
        #         curr_rooms+=1
        #         s+=1
        #     else:
        #         curr_rooms-=1
        #         e+=1
        #     maxrooms = max(curr_rooms , maxrooms)

        # return maxrooms

        #you forgot to soret

        intervals.sort(key = lambda i:i.start)

        minheap = []
        for interval in intervals:
            if minheap and  minheap[0] <= interval.start:
                heapq.heappop(minheap)   
            heapq.heappush(minheap , interval.end)

        return len(minheap)




