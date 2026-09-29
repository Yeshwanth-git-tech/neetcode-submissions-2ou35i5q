class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevend = intervals[0][1]
        res = 0

        # [[1,2],[2,4],[1,4]]
        # [[1,2],[1,4],[2,4]]

        for start , end in intervals[1:]:
            # 1>=2 #it is not , so overlappoping else
            if start >= prevend:
                prevend = end

            else:
                res+=1
                prevend = min(end , prevend)

        return res

                
                
        