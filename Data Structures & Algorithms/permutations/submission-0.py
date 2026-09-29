class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        curr = []

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 

            for n in nums:
                if n in used:
                    continue 

                curr.append(n)
                used.add(n)

                dfs()
                curr.pop()
                used.remove(n)

        dfs()

        return res

        