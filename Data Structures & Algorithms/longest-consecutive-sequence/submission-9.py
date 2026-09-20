class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        #using set data structure O(n)

        seen = set(nums)
        # Iterate the set, not the list. On input with many duplicates like [1,1,1,1,...], the list version re-runs the check for every copy. Same big-O, less work:
        # for n in nums:
        for n in seen:
            if (n-1) not in seen:
                length = 0
                while(n+length) in seen:
                    length+=1
                longest = max(length , longest)

        return longest

        # ##brute force

        # #O(nlogn)

#         if not nums:
#             return 0

#         nums.sort()

      

#         longest = 1
#         current = 1

#         for i in range(1 , len(nums)):
#             if nums[i] == nums[i-1]:
#                 continue

#             if nums[i] == nums[i-1] +1:
#                 current+=1
#             else:
#                 current = 1

#             longest = max(longest , current)

#         return longest

# # Note the sort version is not strictly worse. It uses less space. If someone hands you a memory constraint, sorting wins. Worth saying

            

    