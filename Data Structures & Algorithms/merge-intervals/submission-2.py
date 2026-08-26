class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        #declare it as list
        res=[intervals[0]]
        # res = intervals[0]
        #it is starting from [1 , 5] the fist index, 
        #now it will check with [1 , 3]
        #so 
        for start, end in intervals[1:]:
            lastmax = res[-1][1]
            if start<=lastmax:
                res[-1][1] = max(lastmax , end)
            else:
                res.append([start , end])
        return res



        
