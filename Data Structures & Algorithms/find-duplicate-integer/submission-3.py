class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #this is posssible as len = n+1 as the range is [1 , n] -where n is inclusive
        #[1,2,3,2,2] , range : [1,3] - len n+1 = 3+1 = 4


        #so the oth index is not requried 
        #and the range is alaways from [1, n]

        slow = 0 
        fast = 0
        #that is slow and fast will be comoared ti find the intersection in the floydsc cycle 
        ##so this will give us the intersection then using that we wwill find the
        #2nd slower poineter and the first slow pointer intersection 
        #which is the duplicate
        while True:
            #one time
            slow = nums[slow]
            #two times
            fast = nums[nums[fast]]
            if slow == fast:
                break
    
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            while slow == slow2:
                #we can return nay slow pointer , it will be the same duplicate
                return slow

            












        # hashset = set()

        # for num in nums:
        #     if num in hashset:
        #         return num
        #     hashset.add(num)
        
        

        