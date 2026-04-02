class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]

        # return []    

        hash1={}
        for i , num in enumerate(nums):
            value = target - num
            if value in hash1:
                return([hash1[value], i])
            hash1[num] = i
