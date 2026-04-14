class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap ={}

        # for num in nums:
        #     if num not in hashmap:
        #         hashmap[num] = num
        #     elif num in hashmap:
        #         return True
        #         break
        # return False
            # return True

        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = num
        return False




        