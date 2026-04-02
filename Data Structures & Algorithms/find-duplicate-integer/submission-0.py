class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]

        #cycle

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break

        #so we have sounfd the cycle now lets slow the fast and start from bef
        #reset fast
        fast = nums[0]
        while fast!=slow:
                fast = nums[fast]
                slow = nums[slow]
        return slow