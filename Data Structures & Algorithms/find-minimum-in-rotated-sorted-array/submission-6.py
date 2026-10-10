class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1

        # if nums[l] < nums[r]:
        #     #it is already sorted
        #     res = nums[l]
        #     return res

        #such a comedy if nums[l] <= nums[r]

        while l<=r:
            if nums[l] <= nums[r]:
                res = min(res , nums[l])
                return res
            #now we will chek the middle is in left or right sorted
            m = (l+r)//2 
            
            res = min(res , nums[m])
            
            #middle is in left sorted poriton
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m - 1

