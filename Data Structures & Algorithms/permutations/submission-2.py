class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        used = set()
        res = []
        subset = []
        def backtrack():
            if len(subset) == len(nums):
                res.append(subset[:])
                return 
            
            for n in nums:
                if n in used:
                    continue

                subset.append(n)
                used.add(n)
                backtrack()
                subset.pop()
                used.remove(n)
                
        backtrack()
        return res
