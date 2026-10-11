class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0
        # while fast
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        slow2 = 0
        # while slow:
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
                #return slow2 , both will be at same point

        

        