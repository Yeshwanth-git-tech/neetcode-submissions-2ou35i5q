class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        part = []

        def dfs(i):
            if i>=len(nums):
                res.append(part.copy())
                return 
            part.append(nums[i])
            dfs(i+1)
            part.pop()
            dfs(i+1)

        dfs(0)
        return res


        