class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #there is three ways to do it 
        ##xor
        ##Gauss 
        ##Incremental way of Gauss
        ##this is incremental way  
        #[3,0,1] , len = 3 ,, so i = 0 , nums[i] = 3 3+=0-3 = 0
        #i =1 , 0+=1-0 = 1
        #i = 2 , 1+=2-1 = 2
        #return 2
        
        # res = len(nums)

        # for i in range(len(nums)):
        #     res+= i - nums[i]
        # return res

        ## same concept xor , i ^ nums[i]

        res = len(nums)

        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res


        ##Gauss 

        ##expected sum - actual sum 
        ##n*(n+1)//2 (integer divisioin and will nt gice decimal)
        
        # n = len(nums)

        # res = n*(n+1)// 2 - sum(nums)

        # return res
        