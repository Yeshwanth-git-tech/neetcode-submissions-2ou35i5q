class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for n in nums:
            if n-1 not in seen:
                curr = 0
                while n+curr in seen:
                    curr+=1

                longest = max(curr , longest)

        return longest

