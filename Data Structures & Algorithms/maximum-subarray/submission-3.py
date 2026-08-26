class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadanes
        # Kadane's algorithm uses a simple form of dynamic programming. It runs in O(n) time complexity and O(1) space complexity

        # maxsum = 0

        ##so instead of maxsum , to handle the edge case , -1 , we will use 
        #maxsum = nums[0]

        maxsum = nums[0]
        currsum = 0
        for n in nums:
            if currsum <0:
                currsum = 0

            currsum+=n
            maxsum = max(maxsum, currsum)

        return maxsum