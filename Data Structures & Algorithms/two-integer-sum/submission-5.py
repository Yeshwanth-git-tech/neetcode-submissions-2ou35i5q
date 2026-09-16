class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = set()
        #that why i need hashmap for this , index stored as value
        hashmap = {}

        for i , num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[num] = i
        
