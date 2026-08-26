class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        #declare it as list
        res=[intervals[0]]
        # res = intervals[0]
        #it is starting from [1 , 5] the fist index, 
        #now it will check with [1 , 3]
        #so 
        # lastmax = res[0][1]
        #same as res[-1]
        # for start, end in intervals[1:]:
        #     lastmax = res[-1][1]
        #     if start<=lastmax:
        #         res[-1][1] = max(lastmax , end)
        #     else:
        #         res.append([start , end])
        # return res
        #here we need to have the last element and the 1st index
        #if we give lastmnax[0][1] , 
        # it will only take gthe first elemenmt last index
        lastmax = res[-1][1]

        for start , end in intervals[1:]:

            if start<=lastmax:
                #overlapping 
                lastmax = max(lastmax , end)
                #update the new end
                res[-1][1] = lastmax
            else:
                res.append([start , end])
                #update the new end
                lastmax = end

        return res


        
