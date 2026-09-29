class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        #lamda
    # def getfirst(i):
        # return i[0]

        #intervals.sort(ley = getfirst) #this is same , and not getfirst()


        res = [intervals[0]]


        # for start , end in intervals[1:]:


        for interval in intervals[1:]:
            lastend = res[-1][1]

    
            start = interval[0]
        
            end = interval[1]
  
            # for start , end in interval:
            #     #overlapping
            if start<=lastend:
                lastend = max(end , lastend)
                res[-1][1] = lastend
            else:
                res.append([start , end])

        return res

    
