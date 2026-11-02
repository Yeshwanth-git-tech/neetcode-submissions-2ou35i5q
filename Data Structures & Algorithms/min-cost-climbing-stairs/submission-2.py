class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
     
        cost.append(0)
        #then onyl i+2 , can be done 

        for i in range(len(cost)-3 , -1 , -1):
            cost[i] = min( (cost[i]+cost[i+1]) , (cost[i]+cost[i+2]))

        return min(cost[0] , cost[1])


        #we need the min from step 0 and step1 indx
        