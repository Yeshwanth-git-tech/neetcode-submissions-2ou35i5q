class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        seen = set()
        res = []
        subset = []

        def backtrack():
            if len(subset)==len(nums):
                res.append(subset[:])
                return 


            for n in nums:
                if n in seen:
                    continue
                
                subset.append(n)
                seen.add(n)
                backtrack()
                subset.pop()
                seen.remove(n)

        backtrack()
        return res

                       