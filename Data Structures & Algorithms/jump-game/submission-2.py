class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalpost = len(nums)-1

        for i in range(len(nums)-1 , -1 , -1):
            if i + nums[i]>= goalpost:
                goalpost = i
                #shift our goalpost near to us

        return True if goalpost == 0 else False