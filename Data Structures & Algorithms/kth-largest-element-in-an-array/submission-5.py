class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = nums
        # heapq.heapify(nums)
        

        # #i did if len(heap) this shoukd not reaoeat very basic

        # while len(heap) > k:
        #     heapq.heappop(heap)
        # # print(heap)
        # return heap[0]

        nums.sort()
        return nums[len(nums) - k]
        