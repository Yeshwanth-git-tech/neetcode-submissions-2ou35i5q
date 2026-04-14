class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlongest = 0
        seen = set(nums)
        for num in nums:
            if num-1 not in seen:
                curr_l = 0
                while (num+curr_l) in seen:
                    curr_l+=1
                maxlongest = max(curr_l , maxlongest)
        return maxlongest