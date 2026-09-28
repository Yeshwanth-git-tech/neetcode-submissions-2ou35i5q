class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # print(sum(gas))
        # print(sum(cost))
        # if sum(gas) - sum(cost):
        #     return -1

        #we have to acculumate the total
        # gas=[3,1,1]
        # cost=[1,2,2] # consider for this where start itself at 0 m if we dont accumuate the total there wont be gas for other costs , the i = 0 
        start = 0
        total = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            #we dont need to add this difference total andmaintan the sum of difference as if it is less than 0 then we equate it to zero and find othe part where the difference is greater than 0 ,we are gauranteed to find it as the base case it not true and we dont return -1 

            if total < 0:
                total = 0
                # we have not yet found the index where the gas is positive
                #so increment start 
                start = i+1
                #if we find where total is greater than 0 , then we can manage the cost with the gas
        return start        