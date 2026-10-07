class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helperr(nums[1:]),
                   self.helperr(nums[:-1]), 
                    nums[0])


    def helperr(self , nums):
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = max(n + rob1 , rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
        
        