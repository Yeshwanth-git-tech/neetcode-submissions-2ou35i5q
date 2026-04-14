class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap ={}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = num
            elif num in hashmap:
                return True
                break
        return False
            # return True




        