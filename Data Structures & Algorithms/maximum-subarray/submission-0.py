class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        #like two pointers
        #brute force will take O(n^3)
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum+=n
            maxSub = max(currSum ,maxSub)

        return maxSub

