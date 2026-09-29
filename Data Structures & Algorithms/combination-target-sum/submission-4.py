class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i , curr , total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return 

            
            #including the candidate
            curr.append(nums[i])
            dfs(i , curr , total+nums[i])
#             In Combination Sum, dfs(i, total + nums[i]) means: "I took nums[i], and I'm still allowed to take it again." That's how [2,2,2] gets built: take 2, stay at index 0, take 2 again, and so on, until the total reaches or passes the target.

# Your commented-out dfs(i + 1, curr, total + nums[i]) would allow each number only once. With [2, 3] and target 6, it would miss both [2,2,2] and [3,3]
            # dfs(i+1 , curr , total+nums[i])

            
            #not including the candidate
            curr.pop()

            dfs(i+1 , curr , total)

        dfs(0, [] , 0)

        return res

        