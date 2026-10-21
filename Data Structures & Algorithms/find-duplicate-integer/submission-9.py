class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        # while fast:
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break

        slow2= 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                # return nums[slow]
                #it is already number
                return slow



        

        
        

        