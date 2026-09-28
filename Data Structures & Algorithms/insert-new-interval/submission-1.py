class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #if the newinterval[0] > intervals[i][1] then intervals[i][1] is first else newinterval[1] < intervals[i][0] then new interval is first
        #else if not both the above conditons then 
        #newinterval = min(newinterval[0] ,intervals[i][0] ) max(newinterval[0] , intervals[i][1])
        res = []

        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                #here the new interval might overlap with next interval so we are keeping it
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                #we are returning as the new interval is not overlapping
                res.append(newInterval)
                #dont forget to append all the other intervals
                return res + intervals[i:]
            else:
                #overlapping
                newInterval = [min(newInterval[0] ,intervals[i][0]) , max(newInterval[1] , intervals[i][1])]

        res.append(newInterval)

        return res


