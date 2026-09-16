class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        #if there is no duplicate after parsing all the nums
        return False




        