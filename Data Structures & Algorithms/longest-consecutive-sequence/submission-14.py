class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxlength = 0

        # for n in nums: to avoaif On sqwaure)
        for n in seen:
            curr = 0
            #when the n-1 is not hta tis shte starting point
            if n-1 not in seen:
                while (n + curr) in seen:
                    curr+=1
                maxlength = max(maxlength , curr)

        return maxlength
                
        