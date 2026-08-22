class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l , r  = 0 , len(nums)-1

        

        # res = nums[0]
        

        # while l <=r:
        #     mid = (l+r) // 2
        #     #just checking the min at everystep
        #     res = min(res, nums[mid])
        #     if nums[mid] > nums[r]:
        #         l = mid+1
        #     else:
        #         r = mid - 1
        # return res
        # #  res = min(res, nums[mid])  ← already captured mid!
        # #  r = mid-1  ← safe to exclude mid now ✓


















        l = 0 
        r = len(nums) - 1

        res = nums[0]
        while l <=r:
            #if it is already sorted 
            if nums[l] <= nums[r]:
                res = min(res , nums[l])
                return res
            
            #else find the middle to which part it is in 

            m = (l+r)//2
            res = min(res , nums[m])
            if nums[m] >= nums[l]: # then it is in left sorted portionn
                l = m+1
            else:
                r = m-1


