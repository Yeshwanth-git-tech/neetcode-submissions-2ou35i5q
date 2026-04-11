class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        curr_sum = 0
        for num in nums:
            if num == 1:
                curr_sum +=1
                longest = max(curr_sum , longest)
            else:
                curr_sum = 0
        return longest
        