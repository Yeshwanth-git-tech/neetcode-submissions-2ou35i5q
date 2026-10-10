class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r) // 2
            if nums[m] == target:
                return m

            #we will check the m is in left or right sorted array
            #m is in left sorted array
            if nums[m] >= nums[l]:
                #now to check where is the target in right sorted portion
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m+1

        return -1