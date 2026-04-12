class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket = [0, 0 , 0]

        # for n in nums:
        #     bucket[n] +=1

        # print(bucket)

        # i = 0
        # for num in range(3):
        #     for _ in range(bucket[num]):
        #         nums[i] = num
        #         i+=1

        l = 0
        r = len(nums)-1
        i = 0

        n = len(nums)

        def swap(i , j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        while i <=r:
            if nums[i] == 0:
                swap(l , i)
                l+=1
            elif nums[i] == 2:
                swap(i ,r)
                r-=1
                i-=1
                
            i+=1
               