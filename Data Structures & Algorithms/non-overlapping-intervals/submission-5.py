class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = [intervals[0]]

        cnt = 0

        for start , end in intervals[1:]:
            lastend = res[-1][1]
            if start < lastend:
                cnt+=1
                lastend = min(end , lastend)
                #upodate he result you forhgot
                res[-1][1] = lastend
            else:
                res.append([start , end])

        return cnt
        