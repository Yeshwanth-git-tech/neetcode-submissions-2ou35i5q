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


        minheap = []

        heapq.heappush(minheap , intervals[0].end)

        for interval in intervals[1:]:
            if interval.start>=minheap[0]:
                heapq.heappop(minheap)

            heapq.heappush(minheap , interval.end)

        return len(minheap)