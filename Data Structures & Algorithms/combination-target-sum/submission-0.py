class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i , curr , total):
            #base case
            if total == target:
                res.append(curr.copy())
                return

            #lets check if we are inbound and total > target

            if i >= len(nums) or total > target:
                return 
            #so now lets append the values form nums to our list    
            curr.append(nums[i])
            dfs(i , curr , total+nums[i])

            curr.pop()

            dfs(i +1 , curr , total)

        dfs(0 , [] , 0)

        return res
        