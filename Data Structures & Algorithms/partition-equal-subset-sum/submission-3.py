class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        ##base conditon

        if sum(nums)%2:
            return False

        dp = set()

        dp.add(0)

        target = sum(nums) // 2

        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                #to improve the efficieny if we find the target in dp , then we can return True 
                if t+nums[i] == target:
                    return True
                
                ## taking 1 or 0 in nums[i] 
                #so if we take take the nums[i] , then we add t+nums[i]
                nextDP.add(t + nums[i])
                #if we dont add anything
                nextDP.add(t)
               
            dp = nextDP

        return True if target in dp else False

        

        
