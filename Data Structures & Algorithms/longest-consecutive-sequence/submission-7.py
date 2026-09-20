class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        #using set data structure O(n)

        seen = set(nums)

        for n in nums:
            if (n-1) not in seen:
                length = 0
                while(n+length) in seen:
                    length+=1
                longest = max(length , longest)

        return longest

        ##brute force

        #O(nlogn)
        nums.sort()

        longest = 1
        current = 1

        if not nums:
            return 

        for i in range(1 , len(nums)):
            if nums[i] == nums[i-1]:
                continue

            if nums[i] == nums[i-1] +1:
                current+=1
            else:
                current = 1

            longest = max(longest , current)

        return longest

            

    