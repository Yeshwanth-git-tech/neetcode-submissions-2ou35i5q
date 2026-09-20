class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)

        #res =[1, 1, 1, 1]


        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
            #[1 , 1, 2 , 8]
        
        postfix = 1

        for i in range(len(nums)-1 , -1, -1):
            res[i] *=postfix
            postfix = postfix*nums[i]

        return res








        # res = []
        # total = 1
        # for n in nums:
        #     total*=n
        # for n in nums:
        #     res.append(total//n)

        # return res

        ##for this division technique you have to keep the zero cunt


        #brute force O(n sqaure)
        res = []
        n = len(nums)
        for i in range(n):
            prod = 1
            for j in range(n):
                if i!=j:
                    prod*=nums[j]
            res.append(prod)

        return res
        
        
            
            



