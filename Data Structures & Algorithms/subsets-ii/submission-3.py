class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        subsets = []        
        def subset(i):
            if i>=len(nums):
                res.append(subsets.copy())
                return 
            
            subsets.append(nums[i])
            subset(i+1)
            subsets.pop()
            #again yiu used if here
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            subset(i+1)

        subset(0)
        return res
 