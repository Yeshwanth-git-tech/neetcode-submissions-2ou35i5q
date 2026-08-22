class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1

        while l<=r:
            m = (l+r) // 2
            #base conditon 
            if nums[m] == target:
                return m

            
            #lets check where is m left or right sorted poriton
            if nums[m] >= nums[l]:
                
                #then it is in left sorted portion
                if target > nums[m] or target < nums[l]:
                    #3 , 4, 5, 6, 0 , 1, here target = 6 , 5 is mid
                    #target = 3 , 4 , 5  , 0 , 1 , 2
                    #here 0 ,is the target , 5 is mid
                    l = m+1
                else:
                    r = m-1
            #mid is in right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1
