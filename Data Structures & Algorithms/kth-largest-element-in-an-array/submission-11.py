class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # for n in nums:
        #     heapq.heappush(heap , n)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # return heap[0]

        l = 0
        r = len(nums)-1
        #this is the index we are looking at 
        target = len(nums)-k 

        def quickselect(l , r):
            while l<=r:
                pivot = nums[r]
                p = l
                for i in range(l , r):
                    if nums[i] <= pivot:
                        nums[i] , nums[p] = nums[p] , nums[i]
                        p+=1
                nums[r] , nums[p] = nums[p] , nums[r]

                if target > p:
                    l = p + 1
                    return quickselect(l , r)
                elif target < p:
                    r = p - 1
                    return quickselect(l , r)
                else:
                    return nums[p]
        return quickselect(0, len(nums) - 1)