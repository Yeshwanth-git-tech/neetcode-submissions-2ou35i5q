class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadanes
        # Kadane's algorithm uses a simple form of dynamic programming. It runs in O(n) time complexity and O(1) space complexity

        # maxsum = 0

        ##so instead of maxsum , to handle the edge case , -1 , we will use 
        # maxsum = nums[0]

        # maxsum = nums[0]
        # currsum = 0
        # for n in nums:
        #     # currsum+=n
        #     if currsum <0:
        #         currsum = 0
        #     #here to avoid negative values
        #     currsum+=n
        #     # max(-1 , -1) = -1
        #     maxsum = max(maxsum, currsum)

        # return maxsum

        ##also return the subarray

        maxsum = nums[0]
        currsum = 0
        beststart = bestend = 0
        for i , n in enumerate(nums):
            if currsum < 0:
                currsum = 0
                # start = i

            currsum+=n
            if currsum > maxsum:
                maxsum = currsum
                # beststart = start
                # bestend = i
        # print(nums[beststart:bestend+1])
        return maxsum



        ##bruteforce
        # max_sum = nums[0]
        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i , len(nums)):
        #         curr_sum +=nums[j]

        #         max_sum = max(max_sum, curr_sum)

        # return max_sum