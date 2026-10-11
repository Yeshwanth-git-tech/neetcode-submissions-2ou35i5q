class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = nums
        # heapq.heapify(nums)
        

        # #i did if len(heap) this shoukd not reaoeat very basic

        # while len(heap) > k:
        #     heapq.heappop(heap)
        # # print(heap)
        # return heap[0]

        # nums.sort()
        # return nums[len(nums) - k]

        target = len(nums) - k

        def quickselect(l , r):
            p = l
            pivot = nums[r]
            for i in range(l , r):
                if nums[i] <= pivot:
                    nums[p] , nums[i] = nums[i] , nums[p]
                    p+=1
            nums[p] , nums[r] = nums[r] , nums[p]

            if p == target:
                return nums[p]
            elif p < target:
                l = p+1
                #you have to return here too , basically call the4 function
                return quickselect(l , r)
            else:
                r = p-1
                return quickselect(l , r)


        return quickselect(0 , len(nums)-1)
        