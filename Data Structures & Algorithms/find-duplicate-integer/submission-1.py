class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #this is posssible as len = n+1 as the range is [1 , n] -where n is inclusive
        #[1,2,3,2,2] , range : [1,3] - len n+1 = 3+1 = 4


        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

        

        