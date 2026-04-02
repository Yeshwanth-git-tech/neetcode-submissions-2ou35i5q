class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res  = [1] * (len(nums))

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        #starting at the end of the input array 
        postfix =1
        for i in range(len(nums) -1 , -1, -1):
            #multiplying postfix with the results of prefix
            res[i] *= postfix
            postfix *= nums[i]
        
        return res