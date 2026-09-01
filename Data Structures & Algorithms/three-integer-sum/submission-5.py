class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #so here we will check with a + b + c
        

        nums.sort()
        res=[]
        for i , a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                #just skip it if it is duplicate
                currsum = a + nums[l] + nums[r]
                if currsum > 0:
                    r-=1
                elif currsum <0:
                    l+=1
                else:
                    res.append([a , nums[l], nums[r]])
                    #then to skip duplicates in l and r 
                    #skipping one will take care of right , 
                    #by the above conditons of currsum >0 and currsum<0
                    l+=1
                    #then contonue the lopp again traversing
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return res


        
        