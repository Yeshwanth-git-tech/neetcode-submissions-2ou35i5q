class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 = 0
        # rob2 = 0

        # #so basically

        # #1 , 1 , 3 , 3
        # #here nums[0] = rob1 , nums[1] = rob2 , 3 = n
        # #now m+rob1 or rob2 whichever is max that robber house
        # #now we will switch rob1 to rob2 and rob2 as the max value claculare till here
        # for n in nums:
        #     tmp = max(n + rob1 , rob2)
        #     rob1 = rob2
        #     rob2 = tmp

        # return rob2
       
        memo = {}
        def dfs(i):
            if i>=len(nums):
                return 0

            if i in memo:
                return memo[i]
            
            combine = nums[i] + dfs(i+2)
            skip = dfs(i+1)
            memo[i] = max(skip , combine)

            return memo[i]

         

        return dfs(0)



        