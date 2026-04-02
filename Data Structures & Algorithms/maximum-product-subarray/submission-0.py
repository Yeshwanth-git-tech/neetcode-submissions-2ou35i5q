class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #[-1 , 8] - we can directly return 8
        currMax, currMin = 1 , 1
        for n in nums:
            if n == 0:
                currMax, currMin = 1 , 1
            #Stores previous currMax * n to avoid overwriting before updating currMin

            tmp = n*currMax
            currMax = max(n*currMax , n*currMin , n) #i'm adding n alos has [-1 , 8] -here the max is just the 8
            currMin = min(tmp ,  n*currMin , n)
            #Tracks global max product seen so far
            res = max(res , currMax)
        return res