class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalpost = len(nums) -1 

        for i in range(len(nums)-1 , -1 , -1):
            #from the index maximum jump
            if i + nums[i] >= goalpost:
                #shift the goal post - greedy
                goalpost = i

        return True if goalpost == 0 else False