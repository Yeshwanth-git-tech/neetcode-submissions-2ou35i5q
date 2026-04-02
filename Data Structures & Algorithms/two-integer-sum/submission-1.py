class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}

        #hasmapwill have the key as number in the value as index position

        for i , num in enumerate(nums):
            value = target - num
            if value in hashmap:
                return [hashmap[value], i]
            hashmap[num] = i
