class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i , num in enumerate(nums):
            res = target - num
            if res in hashmap:
                return [hashmap[res] , i]
            hashmap[num] = i
