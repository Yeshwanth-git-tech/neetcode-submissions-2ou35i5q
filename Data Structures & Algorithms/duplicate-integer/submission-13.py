class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False

        ###brute force - O(n^2) , 

        seen = {}

        for i , n in enumerate(nums):
            if n in seen:
                return True
            #else we have not yet added so lets add it
            seen[n] = i
        #after iterating through all the numbers
        #space is O(n) , time complexity is O(n) as we iterate only once
        return False

        #we can use set 
        ## 
        # seen = {}

        # for i , n in enumerate(nums):
        #     if n in seen:
        #         return True
        #     #else we have not yet added so lets add it
        #     seen[n] = i
        # #after iterating through all the numbers
        # #space is O(n) , time complexity is O(n) as we iterate only once
        # return False

        #we can use set
        #seen.add(n) , same space and time complexity as hashmap That makes the dict the wrong tool. A set fits because you only care whether you've seen the value, not where.
        #seen.add(n) , same space and time complexity as hashmap

        seen = set()

        for n in nums:
            seen.add(n)

        return len(seen) != len(nums)


        

        