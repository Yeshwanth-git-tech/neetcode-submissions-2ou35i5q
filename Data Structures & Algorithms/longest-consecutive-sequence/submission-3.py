class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset =set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numset:
                l=0# so if the n-1 is not there then it is the lowest in its sequence
                while (n+l) in numset:
                    l+=1
                    longest = max(l , longest)
        return longest


