class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        #lets sort it 
        nums.sort()

        for i , num in enumerate(nums):
            # to avoid duplicate triplets
            if i > 0 and num == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            
            while l < r:
                threesum = num + nums[l] + nums[r]
                if threesum > 0 :
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    #lets check whether the second and third position are 
                    #same if then we will have to increment 
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
