class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
    #     #so basically , l , r 

    #     #k is the window length
    #     l = 0
    #     r = len(numbers)-1

    #     while l < r:
    #         currsum = numbers[l] + numbers[r]
    #         if currsum < target:
    #             l+=1
    #         elif currsum > target:
    #             r-=1
    #         else:
    #             return[l+1 , r+1]
    # # vs Two Sum 1:
    # # unsorted → need hashmap → O(n) space
    
    # # vs Two Sum 2:
    # # sorted → two pointers → O(1) space ✓




























        l = 0
        r = len(numbers) - 1
        currsum = 0
        while l<r:
            currsum = numbers[l] + numbers[r]
            if currsum < target:
                l+=1
            elif currsum > target:
                r-=1
            else:
                return [l+1 , r+1]
            # else:
            #     r-=1
                


