class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        subset = []
        res = []

        def backtrack(i , total):
            if total == target:
                res.append(subset[:])
                return
            if total > target or i>=len(candidates):
                return 
            
            subset.append(candidates[i])
            backtrack(i+1 , total+candidates[i])
            
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            
            backtrack(i+1  , total)
            

        backtrack(0 , 0)
        return res