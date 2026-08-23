class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest = 0

        # seen = set(nums)

        # for n in nums:
        #     # while n-1 not in seen:
        #     if (n-1) not in seen:
        #         length = 0
        #         while (n+length) in seen:
        #             length +=1
        #         longest = max(longest , length)

        # return longest
        nums.sort()
        longest = 1
        current = 1
        if not nums:
            return 0

        for i in range(1 , len(nums)):
            #duplicate
            if nums[i] == nums[i-1]:
                continue
            #consecutive
            
            if nums[i] == nums[i-1] + 1:
                current+=1
            else:
                current = 1

            longest = max(longest , current)

        return longest

            

    