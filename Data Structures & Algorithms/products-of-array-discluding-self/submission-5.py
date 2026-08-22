class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix
            prefix = nums[i]*prefix

        postfix = 1

        # print(result)


        for i in range(len(nums)-1, -1 , -1):
            result[i]*=postfix
            postfix = nums[i] * postfix
            # print(result)
            
        return result



