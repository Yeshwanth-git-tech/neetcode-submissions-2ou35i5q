class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = float("infinity")
        #already sorted
        if nums[l] <= nums[r]:
            return min(nums[l] , nums[r])

        while l<=r:
            #base case 
            m = (l+r)//2
        #     print("here" , m)
        #     #may be we found it 
            res = min(res , nums[m])
        #     #m is in left sorted portion
        #     print("numsm" , nums[m])
        #     print("numsl" , nums[l])
        #     if nums[m] >= nums[l] and nums[m] > nums[r]:
        #         l = m + 1
        #         print("ll" , l , nums[l])
        #     else:
        #         r = m - 1

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return res

    
                
        