class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        steps = 0
        # fasthest = 0
        #or while r >=len(nums)
        while r<len(nums)-1:
            farthest = 0
            #bfs
            #so first we will check the jump value of 2 in nums = [2,4,1,1,1,1]
            #r+1 to inclued the first index
            #so 2 , fatherst  = max(0 , 0+2) = 2
            #l = 1
            #r = 2
            #steps = 0+1 =1
            #now check for the next farther , since we start r = 0 , we will include 4 (1th index) anyways
            #farthest =max(2 , 1+4) = 5 
            #steps+=1 = 1+1 = 2, reached the goail

            for i in range(l , r+1):
                farthest = max(farthest , i+nums[i])
            l = r+1
            r = farthest
            steps+=1

        return steps
            