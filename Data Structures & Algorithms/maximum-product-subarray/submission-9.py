class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currmax= 1
        currmin = 1
        for n in nums:
            temp = currmax * n
            #so we trach currmax and currmin of each position
            currmax = max(n , temp , currmin*n)
            currmin = min(n , temp , currmin*n)
            res = max(res , currmax)


        return res

        n = 5

# temp = -3 × 5 = -15
# currmax = max(5, -15, -24×5 = -120) = 5
# currmin = min(5, -15, -120) = -120
# res stays 8.

# Return 8, from the subarray [2, 4].

# Why track currmin

# A negative number flips the signs, so the most negative product can become the most positive one later.
# For example, if another negative came after 5, then -120 × negative would become a big positive.
        # res = nums[0]
        # for i in range(len(nums)):
        #     curr = 1
        #     for j in range(i, len(nums)):
        #         curr*=nums[j]
        #         res = max(res , curr)

        # return res

        # ##O(n^2)
                
        