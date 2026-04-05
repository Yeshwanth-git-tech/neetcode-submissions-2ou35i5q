class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmax , currmin = 1 , 1

        for n in nums:
            temp = currmax
            currmax = max (temp*n , currmin*n , n)
            currmin = min(temp*n , currmin*n , n)
            res = max(currmax , res)
        return res
            