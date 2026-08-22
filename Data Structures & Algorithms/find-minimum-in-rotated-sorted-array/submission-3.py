class Solution:
    def findMin(self, nums: List[int]) -> int:
        #so this is a two pointer qn 

        l , r = 0 , len(nums)-1

        res = nums[0]
        while l<=r:

            #base condition 

            #when we reach the sorted array portion , 
            #either left or right or completly

            ##
            if nums[l] <= nums[r]:
                res = min(res , nums[l])
                return res
                
                # we will exit when this is true

            m = (l+r)//2 #logn
            #what if middle is the min
            res = min(res , nums[m])

            #if m is in left sorted portion
            #condtion to look for min
            if nums[m] >= nums[l]:
                #look left
                #shift the right pointer
                l=m+1
            else:
                #look right
                r=m-1


            

