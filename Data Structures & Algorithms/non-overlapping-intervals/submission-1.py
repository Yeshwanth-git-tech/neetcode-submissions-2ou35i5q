class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort
        #so basically we will check whether the [1 , 3] , [2 , 4] 
        #check whether 3 <= 2 , then it is not overlappin , but here it is 2< 3 else conditon , then we will
        #have to check the maxend , which end is max that interval needs to be removed ,
        #so that it will avoid overllapping many other intervals
        #so just chaning the end will be enough and that end will be compared to the next interval 



        # intervals.sort()
        # #so here default , start will be used to sort , if start is same for two intervals then the end will
        # #be used
        # res = 0
        # prevend = intervals[0][1]

        # for start , end in intervals[1:]:
        #     if prevend <= start:
        #         #not overlapping 
        #         #just updating 
        #         prevend = end
        #     else:
        #         #overlapping and update the count
        #         res+=1
        #         #inorder to remove the max end interval
        #         prevend = min(end ,prevend)

        # return res



        res = 0
        intervals.sort()

        prevend = intervals[0][1]

        for start , end in intervals[1:]:
            #so wwe will check if the prev is greater or eeqal and smaller to end
            if start >= prevend:
                #not overlapping
                prevend = end
            else:
                res+=1
                prevend = min(prevend , end)
        return res

























