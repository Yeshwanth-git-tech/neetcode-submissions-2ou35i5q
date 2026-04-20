class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r  = 0 , len(nums)-1

        

        res = nums[0]
        

        while l <=r:
            mid = (l+r) // 2
            #just checking the min at everystep
            res = min(res, nums[mid])
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid - 1
        return res
        #  res = min(res, nums[mid])  ← already captured mid!
        #  r = mid-1  ← safe to exclude mid now ✓
            
