class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        res = nums[l]

        

        while l<=r:
            m = (l+r)//2
            #now we have entered the sorted portion ,so this is after moving the left and right
            # if nums[l] <= nums[r]:
            #     res = min(res , nums[l])
            # res = min(res, nums[m])
            #may be middle isistfel the min

            #we have to check if the m is in left or right sorted
            # if nums[m] >= nums[l]:
            #     l = m + 1
            # else:
            #     r = m - 1
            res = min(res , nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1


                #left sorted portion
        return res