class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = 1
        currmin = 1
        res = nums[0]

        for n in nums:
            temp = currmax * n
            currmax = max(n, temp , currmin*n)
            currmin = min(n, temp , currmin*n)
            res = max(res , currmax)

        return res