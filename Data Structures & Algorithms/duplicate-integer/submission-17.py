class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


        # nums.sort()

        # for i in range(1 , len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False




        # for x in nums:
        #     i = abs(x) - 1
        #     if nums[i] < 0:
        #         return True
        #     #we mark the 1 num , index for it 0 , change it to negative marked
        #     nums[i] = -1 *(nums[i])
        # return False

        

