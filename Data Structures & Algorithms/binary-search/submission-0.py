class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<=r:
            # m = (l+r)//2
            # to avoid overflow in c and java , as python handles large number
            m = l+ (r-l)//2

            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1 
            else:
                return m

        #if it is not available
        return -1

