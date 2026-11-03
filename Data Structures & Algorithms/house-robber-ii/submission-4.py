class Solution:
    def rob(self, nums: List[int]) -> int:

        return max( self.help_rob(nums[1:]), 
                    self.help_rob(nums[:-1]), 
                    nums[0])

    def help_rob(self , nums_list):
        rob1 = 0
        rob2 = 0

        for n in nums_list:
            temp = max(rob1 +n , rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        