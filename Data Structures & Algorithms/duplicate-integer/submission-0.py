class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap={}
        # for num in nums:
        #     if num in hashmap:
        #         return True
        #     hashmap[num] = True
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
                    

         