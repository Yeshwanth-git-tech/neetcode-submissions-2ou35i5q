"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i:i.start)

        #base conditon
        if not intervals:
            return True

        prevend = intervals[0].end

        for i in intervals[1:]:
            if i.start >= prevend:
                #just update the end , not overlapping
                prevend = i.end

            else:
                return False

        return True
