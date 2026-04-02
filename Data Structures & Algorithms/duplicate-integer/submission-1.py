class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap={}
        # for i , num in enumerate(nums):
        #     if num in hashmap:
        #         return True
        #     hashmap[num] = i
        # return False

        hashset=set()
        for  num in nums:
            if num in hashset:
                return True
            hashset.add(num) 
        return False

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # l,r = 0 , len(nums)-1 
        # # print(len(nums)-1)
 
        # while r < len(nums):
        #     while nums[l]!=nums[r]:
        #         r-=1
        #     while nums[l]!=nums[r]:
        #         l+=1
        #     if nums[l] == nums[r]:
        #         return True
            
        #     return False
        
           

         