class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
    

        for n in nums:
            if n!=val:
                res.append(n)


        if res:
            for i in range(len(res)):
                nums[i] = res[i]
        
        nums = nums[:len(nums)-len(res)]

        print(nums)

        return len(res)