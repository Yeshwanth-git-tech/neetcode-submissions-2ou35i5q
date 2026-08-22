class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = max(nums)
        # currmax , currmin = 1 , 1

        # for n in nums:
        #     temp = currmax
        #     currmax = max (temp*n , currmin*n , n)
        #     currmin = min(temp*n , currmin*n , n)
        #     res = max(currmax , res)
        # return res

        # #3max sum - kadanes algorithm
        # # curr_sum = 0
        # # res = nums[0]

        # # for n in nums:
        # #     if curr_sum < 0:
        # #         curr_sum = 0
        # #     curr_sum=n
        # #     print(curr_sum)
        # #     res = max(res , curr_sum)
        # # return res




        # maxsub = nums[0]
        # curproduct = 1
        # #base conditon
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return 0
        # for n in nums:
        #     if curproduct < 1:
        #         curproduct = 1
        #     curproduct *=n
        #     maxsub = max(maxsub, curproduct)
        #     if maxsub == 1:
        #         return 0
        # return maxsub


        res = max(nums)
        curmax = 1
        curmin = 1

        for n in nums:
            if n ==0:
                curmax , curmin = 1 , 1
            tmp = n *curmax
            curmax = max(n *curmax , n*curmin , n)
            # curmin = min(n *curmax , n*curmin , n)
            curmin = min(tmp , n*curmin , n)

            res = max(curmax , res)
        return res























        
            