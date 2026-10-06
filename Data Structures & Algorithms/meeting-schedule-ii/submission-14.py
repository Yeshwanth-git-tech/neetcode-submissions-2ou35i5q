"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
    
        if not intervals:
            return 0

        intervals.sort(key = lambda i:i.start)


        # minheap = []

        # heapq.heappush(minheap , intervals[0].end)

        # for interval in intervals[1:]:
        #     if interval.start>=minheap[0]:
        #         heapq.heappop(minheap)

        #     heapq.heappush(minheap , interval.end)

        # return len(minheap)


        start = sorted([i.start for i in intervals])

        end = sorted([i.end for i in intervals])

        s = 0
        e = 0
        curr_rooms = 0
        max_rooms = 0
        while s < len(intervals):
            if start[s] < end[e]:
                curr_rooms+=1
                s+=1
            else:
                e+=1
                curr_rooms-=1

            max_rooms = max(max_rooms , curr_rooms)


        return max_rooms
