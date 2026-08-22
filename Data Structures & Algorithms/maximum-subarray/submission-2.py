class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadanes
        #its like a sliding winfow 

        maxsub = nums[0]
        #logic is if we find prefix negative right , then we will drop it 
        cursum = 0

        for n in nums:
            if cursum < 0:
                #so that prefix is not negative
                cursum = 0
            cursum+=n
            #update the maxsub
            maxsub = max(maxsub , cursum)

        return maxsub
