class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minheap = []

        # for n in nums:
        #     heapq.heappush(minheap , n)
        #     if len(minheap) >k:
        #         heapq.heappop(minheap)

        # return minheap[0]

        target = len(nums) - k 

        def quickselect(l , r):
            pivot = nums[r]
            p = l
            for i in range(l , r):
                if nums[i] <= pivot:
                    nums[i] , nums[p] = nums[p] , nums[i]
                    p+=1
            nums[r] , nums[p] = nums[p] , nums[r]

            if p == target:
                return nums[p]
            elif p < target:
                l = p + 1
                return quickselect(l , r)
            else:
                r = p - 1
                return quickselect(l , r)
        return quickselect(0 , len(nums)-1)