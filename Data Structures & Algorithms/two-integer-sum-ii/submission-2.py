class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #so basically , l , r 

        #k is the window length
        l = 0
        r = len(numbers)-1

        while l < r:
            currsum = numbers[l] + numbers[r]
            if currsum < target:
                l+=1
            elif currsum > target:
                r-=1
            else:
                return[l+1 , r+1]
        # to avoid any edge case of empty list input
        # return [] if len(numbers)
        return [] if len(numbers) == 0 else [l+1 , r+1]

