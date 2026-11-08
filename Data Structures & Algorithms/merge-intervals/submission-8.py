class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        res = [intervals[0]]
        print(res[-1][1])

        for start , end in intervals[1:]:
            lastend = res[-1][1]
            print(lastend)

            if start <= lastend:
                lastend = max(end ,lastend)
                res[-1][1] = lastend
                #merge done 
            else:
                res.append([start , end])

        return res
